import collections
import json

import piemap.projections as pr


NEEDED_NUMBER_OF_AXIS_MAX = 16
NULL_STR_REP = 'NULL'
REC_SEP = ';'
ROW_SEP = '\n'


def dumps(config):
    """Dump configuration into string."""
    return json.dumps(config)


def dump(config, handle):
    """Dump configuration into JSON file via handle."""
    return json.dump(config, handle)


def loads(text):
    """Load configuration from string."""
    return NotImplemented


def load(handle):
    """Load configuration from JSON file handle."""
    return json.load(handle)


def default_linear():
    """DRY."""
    return {
        'AXIS_INDEX': '',
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_MIN': 0.00,
        'AXIS_LIMIT': 0.80,
        'AXIS_MAX': 1.00,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MIN_FOLDED': False,
        'AXIS_VALUE': NULL_STR_REP,
        'AXIS_UNIT': '1',
    }


def default_keys():
    """DRY."""
    return list(default_linear().keys())


def default_values():
    """DRY."""
    return list(default_linear().values())


def default_folded():
    """DRY."""
    return {
        'AXIS_INDEX': '',
        'AXIS_NAME': 'DimensionFolded',
        'AXIS_TYPE': 'FOLDED',
        'AXIS_MIN': 0.00,
        'AXIS_LIMIT': 0.80,
        'AXIS_MAX': 1.00,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MIN_FOLDED': False,
        'AXIS_VALUE': NULL_STR_REP,
        'AXIS_UNIT': 'dB',
    }


def unsafe(text):
    """TODO(sthagen) keep/drop list applies here."""
    return text


def is_numeric(text):
    """Migration artifact."""
    try:
        _ = float(text)
        return True
    except TypeError:
        return False


def parse(text):
    """Parse the DSL contained in text."""
    axis_values_rows_req_string = ''
    has_index_collision = False
    has_index_order_mismatch = False

    info_queue, some_axis_maps = [], []
    if not text.strip():
        some_axis_maps.append(default_linear())
        some_axis_maps[0]['AXIS_INDEX'] = 0
        
        some_axis_maps.append(default_linear())
        some_axis_maps[1]['AXIS_INDEX'] = 1
        some_axis_maps[1]['AXIS_NAME'] = 'Dimension2'
        
        some_axis_maps.append(default_folded())
        some_axis_maps[2]['AXIS_INDEX'] = 2
        info_queue.append('Default used, since no input given.')
    else:
        axis_values_rows_req_string = unsafe(text)
        axis_values_rows_req = [row for row in axis_values_rows_req_string.split(ROW_SEP) if row.strip()]
        n_axis_rows_req = len(axis_values_rows_req)
        for n, row_string in enumerate(axis_values_rows_req[:NEEDED_NUMBER_OF_AXIS_MAX]):  # Was: array_slice(axis_values_rows_req, 0, NEEDED_NUMBER_OF_AXIS_MAX)
            axis_values = default_values()
            axis_values_cand = row_string.split(REC_SEP)
            if len(axis_values) == len(axis_values_cand):
                for i, v in axis_values_cand:
                    if v != '':
                        axis_values[i] = v

            axis_map = dict(zip(default_keys(), axis_values))
            numeric_axis_types = ('LINEAR', 'FOLDED')
            if axis_map['AXIS_INDEX'] == '':
                axis_map['AXIS_INDEX'] = n
            else:
                index_cand = str(axis_map['AXIS_INDEX'])
                i_cfc = str(int(index_cand))
                axis_map['AXIS_INDEX'] = int(i_cfc)
                if index_cand != i_cfc:  # Was !== in PHP
                    info_queue.append(f"NOK '{index_cand}' index requested, accepted as '{i_cfc}'")
                else:
                    info_queue.append(f" OK {index_cand}' index requested, accepted as '{i_cfc}'")

            if axis_map['AXIS_TYPE'] in numeric_axis_types:
                axis_map['AXIS_MIN'] = pr.min_from_limit_max(axis_map['AXIS_LIMIT'], axis_map['AXIS_MAX'])
                if axis_map['AXIS_VALUE'] != NULL_STR_REP and not is_numeric(axis_map['AXIS_VALUE']):
                    axis_map['AXIS_VALUE'] = NULL_STR_REP

            if axis_map['AXIS_TYPE'] == 'FOLDED':
                axis_map['AXIS_LIMIT_FOLDED'] = pr.limit_folded_from_limit_max(axis_map['AXIS_LIMIT'], axis_map['AXIS_MAX'])
                axis_map['AXIS_MIN_FOLDED'] = pr.min_folded_from_limit_max(axis_map['AXIS_LIMIT'], axis_map['AXIS_MAX'])

            axis_values = list(axis_map.keys())
            some_axis_maps.append(axis_map)

        n_axis_rows = len(some_axis_maps)
        if n_axis_rows_req > n_axis_rows:
            info_queue.append(f'{n_axis_rows_req} dimensions requested, but only {n_axis_rows} accepted. Maximum is {NEEDED_NUMBER_OF_AXIS_MAX}')

        best_effort_re_order_map = {}
        collect_index_cand_list = []
        for x, data in enumerate(some_axis_maps):
            index_cand = data['AXIS_INDEX']
            i_cfc = int(index_cand)
            collect_index_cand_list.append(i_cfc)
            if not is_numeric(index_cand) or i_cfc != index_cand or index_cand < 0 or index_cand >= n_axis_rows:
                has_index_collision = True
                conflict_reason = 'NO_INTEGER'
                if i_cfc != index_cand:
                    conflict_reason = 'DC_INTEGER'

                if index_cand < 0:
                    conflict_reason = 'LT_ZERO'

                elif index_cand >= n_axis_rows:
                    conflict_reason = 'GT_NROW'

                info_queue.append(f'Conflicting index rules. Failing IndexCand is {index_cand}, reason is {conflict_reason}')

            if index_cand != x:
                has_index_order_mismatch = True
                info_queue.append(f'Index positions not ordered. Misplaced IndexCand is {index_cand}, found at {x}')

            best_effort_re_order_map[index_cand] = data

        collect_index_cand_set = set(collect_index_cand_list)
        if len(collect_index_cand_set) != len(collect_index_cand_list):
            has_index_collision = True
            hist = collections.Counter(collect_index_cand_list)
            blame_list = []
            for xx, nn in hist.items():
                if nn != 1:
                    blame_list.append(xx)

            blame_list.sort()
            info_queue.append(f'Conflicting index positions. Failing IndexCand/s is/are [{", ".join(blame_list)}], reason is NONUNIQUE_INDEX')

        if not has_index_collision and has_index_order_mismatch:
            some_axis_maps = []
            for k, data in sorted(best_effort_re_order_map.items()):
                some_axis_maps.append(data)

    """
    $normalizedInputDataRows = array();
    foreach($someAxisMaps as $x => $data) {
        $axisValues = array_values($data);
        $normalizedInputDataRows[] = implode(";",$axisValues);
    }
    //DEBUG echo '<pre>ReAssembledRows:'."\n".print_r($normalizedInputDataRows,True).'</pre>';
    $normalizedInputDataString = implode("\n",$normalizedInputDataRows);
    //DEBUG echo '<pre>ReAssembledNormalizedInput:'."\n".print_r($normalizedInputDataString,True).'</pre>';
    echo 'AxisSpecTest: '."\n";
    echo '<form style="display:inline;" method="post" action="'.$_SERVER['PHP_SELF'].'">'."\n";
    echo '<textarea style="font-sice:small;" cols="80" rows="16" name="AXIS_SPEC_ROWS">'.$normalizedInputDataString.'</textarea>'."\n";
    echo '<input type="submit" name="Subme" value="parse" />'."\n";
    echo '</form>'.'<br />'."\n";
    echo '[<a href="'.$_SERVER['PHP_SELF'].'">RESET</a>] to some default to get started.<br />'."\n";
    //echo 'Implicit Keys: '.implode(';',$axisDefaultKeys).'<br />'."\n";
    echo '<pre>';
    echo 'Testing Module: '.$_SERVER['PHP_SELF']."\n";
    $infoQueue[] = 'TestInput: AXIS_SPEC_ROWS=<pre>'."\n".$axisValuesRowsReqString.'</pre>'."\n";
    echo '  TestOutput[0]:'."\n";
    echo '$someAxisMaps='."\n";
    //DEBUG echo print_r($someAxisMaps,True);
    echo '</pre>';
    echo '<table style="width:75%;"><tr><th>Laufd.Nr.</th><th>Name</th><th>Type</th><th>Min</th><th>Limit</th><th>Max</th><th>LimitFolded</th><th>MinFolded</th><th>Value</th><th>Unit</th></tr>'."\n";
    foreach($someAxisMaps as $i => $data) {
        $displayRow = array_values($data);
        echo '<tr><td>';
        echo implode('</td><td>',$displayRow);
        echo '</td></tr>';
    }
    echo '</table>'."\n";
    if($infoQueue) {
        echo '<h2>Info:</h2>';
        echo '<ul><li>';
        echo implode('</li><li>',$infoQueue);
        echo '</li></ul>';
    }
    echo '</body>'."\n";
    echo '</html>'."\n";
    """
    return some_axis_maps, info_queue
