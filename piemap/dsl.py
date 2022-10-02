import collections
import json

import piemap.projections as pr
from piemap import PIPE, SEMI, log

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
        'AXIS_META': '',
    }


def default_keys():
    """DRY."""
    return list(default_linear().keys())


def default_linear_values():
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
        'AXIS_META': '',
    }


def default_folded_values():
    """DRY."""
    return list(default_folded().values())


def unsafe(text):
    """TODO(sthagen) keep/drop list applies here."""
    return text


def is_numeric(text):
    """Migration artifact."""
    try:
        _ = float(text)
        return True
    except (TypeError, ValueError):
        return False


def maybe_int(value):
    """Rococo."""
    if float(value) == float(int(float(value))):
        return int(value)

    return value


def compact_value(text):
    """HACK A DID ACK ..."""
    if not is_numeric(text):
        return text

    try:
        as_int = int(text)
        return as_int
    except (TypeError, ValueError):
        return float(text)


def example_default():
    """Maybe not wanted but matches reference behavior."""
    some_axis_maps = [default_linear()]
    some_axis_maps[0]['AXIS_INDEX'] = 0

    some_axis_maps.append(default_linear())
    some_axis_maps[1]['AXIS_INDEX'] = 1
    some_axis_maps[1]['AXIS_NAME'] = 'Dimension2'

    some_axis_maps.append(default_folded())
    some_axis_maps[2]['AXIS_INDEX'] = 2

    return some_axis_maps, ['Default used, since no input given.']


def parse(text: str):
    """Parse the DSL contained in text."""
    if not text.strip():
        return example_default()

    has_index_collision = False
    has_index_order_mismatch = False

    info_queue, some_axis_maps = [], []
    axis_values_rows_req_string: str = unsafe(text)
    axis_values_rows_req = [row.strip() for row in axis_values_rows_req_string.split(ROW_SEP) if row.strip()]
    n_axis_rows_req = len(axis_values_rows_req)
    for n, row_string in enumerate(
        axis_values_rows_req[:NEEDED_NUMBER_OF_AXIS_MAX]
    ):  # Was: array_slice(axis_values_rows_req, 0, NEEDED_NUMBER_OF_AXIS_MAX)

        axis_values = default_folded_values() if ';FOLDED;' in row_string else default_linear_values()
        axis_values_cand = row_string.split(REC_SEP)
        log.info(f'__{"FOLDED" if ";FOLDED;" in row_string else "NO_FOLD"}__')
        log.info(f'has axis_values[{len(axis_values)}]({axis_values})')
        if len(axis_values) >= len(axis_values_cand):
            kks = default_keys()
            for i, v in enumerate(axis_values_cand):
                if v != '':
                    be_v = compact_value(v)
                    log.debug(f'[{i}]( == {kks[i]}): ({axis_values[i]}) --> ({be_v})')
                    axis_values[i] = be_v
                else:
                    log.debug(f'[{i}]( == {kks[i]}): ({axis_values[i]}) kept ({axis_values[i]})')
        if len(axis_values) > len(axis_values_cand):
            kks = default_keys()
            for i, v in enumerate(axis_values[len(axis_values_cand) :], start=len(axis_values_cand)):
                log.debug(f'[{i}]( == {kks[i]}): ({axis_values[i]}) untouched ({axis_values[i]})')

        log.info(f'has axis candidate[{len(axis_values_cand)}]({axis_values_cand})')
        axis_map = dict(zip(default_keys(), axis_values))
        log.info(f'... axis map is ({axis_map})')
        numeric_axis_types = ('LINEAR', 'FOLDED')
        if axis_map['AXIS_INDEX'] == '':
            log.info(f"has index idea({axis_map['AXIS_INDEX']}) is False?")
            log.info(f'... axis map is ({axis_map})')
            axis_map['AXIS_INDEX'] = n
            i_cfc = axis_map['AXIS_INDEX']
        else:
            print()
            log.info(f"has index idea({axis_map['AXIS_INDEX']}) is True")
            index_cand = str(axis_map['AXIS_INDEX'])
            if is_numeric(index_cand) and float(index_cand) == float(int(float(index_cand))):
                log.info(f'is_numeric({index_cand}) is True')
                i_cfc = str(maybe_int(index_cand))
                axis_map['AXIS_INDEX'] = int(i_cfc)
                if index_cand != i_cfc:  # Was !== in PHP
                    info_queue.append(f'NOK index ({index_cand}) requested, accepted as ({i_cfc})')
                else:
                    info_queue.append(f' OK index ({index_cand}) requested, accepted as ({i_cfc})')
            else:
                log.info(f'is_numeric({index_cand}) is False')
                i_cfc = str(n)
                info_queue.append(
                    f'NOK invalid index ({index_cand}) requested, accepted per parsing order as ({i_cfc})'
                )
        if axis_map['AXIS_TYPE'] in numeric_axis_types:
            if axis_map['AXIS_TYPE'] == 'LINEAR':
                if is_numeric(axis_map['AXIS_LIMIT']) and is_numeric(axis_map['AXIS_MAX']):
                    axis_map['AXIS_MIN'] = maybe_int(
                        pr.min_from_limit_max(axis_map['AXIS_LIMIT'], axis_map['AXIS_MAX'])
                    )
                else:
                    info_queue.append(
                        f"NOK limit({axis_map['AXIS_LIMIT']}) and max({axis_map['AXIS_MAX']}) not both numeric,"
                        f" ignored {axis_map['AXIS_TYPE'].lower()} axis at index ({i_cfc})"
                    )
                if axis_map['AXIS_VALUE'] != NULL_STR_REP and not is_numeric(axis_map['AXIS_VALUE']):
                    axis_map['AXIS_VALUE'] = NULL_STR_REP
            else:  # axis_map['AXIS_TYPE'] == 'FOLDED':
                log.info(f'... claim of FOLDED is True? Axis map is ({axis_map})')
                if is_numeric(axis_map['AXIS_LIMIT']) and is_numeric(axis_map['AXIS_MAX']):
                    axis_map['AXIS_MIN'] = maybe_int(
                        pr.min_from_limit_max(axis_map['AXIS_LIMIT'], axis_map['AXIS_MAX'])
                    )
                    axis_map['AXIS_LIMIT_FOLDED'] = maybe_int(
                        pr.limit_folded_from_limit_max(axis_map['AXIS_LIMIT'], axis_map['AXIS_MAX'])
                    )
                    axis_map['AXIS_MIN_FOLDED'] = maybe_int(
                        pr.min_folded_from_limit_max(axis_map['AXIS_LIMIT'], axis_map['AXIS_MAX'])
                    )
                else:
                    info_queue.append(
                        f"NOK limit({axis_map['AXIS_LIMIT']}) and max({axis_map['AXIS_MAX']}) not both numeric,"
                        f' ignored folded axis at index ({i_cfc})'
                    )

        some_axis_maps.append(axis_map)

    n_axis_rows = len(some_axis_maps)
    if n_axis_rows_req > n_axis_rows:
        info_queue.append(
            f'{n_axis_rows_req} dimensions requested, but only {n_axis_rows} accepted.'
            f' Maximum is {NEEDED_NUMBER_OF_AXIS_MAX}'
        )

    best_effort_re_order_map = {}
    collect_index_cand_list = []
    for x, data in enumerate(some_axis_maps):
        index_cand = data['AXIS_INDEX']
        if is_numeric(index_cand):
            i_cfc = int(index_cand)
        else:
            i_cfc = x
        collect_index_cand_list.append(i_cfc)
        if not is_numeric(index_cand) or i_cfc != index_cand or index_cand < 0 or index_cand >= n_axis_rows:
            has_index_collision = True
            conflict_reason = 'NO_INTEGER'
            if i_cfc != index_cand:
                conflict_reason = 'DC_INTEGER'

            if is_numeric(index_cand) and index_cand < 0:
                conflict_reason = 'LT_ZERO'

            elif is_numeric(index_cand) and index_cand >= n_axis_rows:
                conflict_reason = 'GT_NROW'

            info_queue.append(
                f'Conflicting index rules. Failing candidate is ({index_cand}), reason is {conflict_reason}'
            )
            some_axis_maps[x]['AXIS_INDEX'] = x

        if index_cand != x:
            has_index_order_mismatch = True
            info_queue.append(f'Index positions not ordered. Misplaced candidate is {index_cand}, found at {x}')

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
        info_queue.append(
            f'Conflicting index positions. Failing candidate/s is/are [{", ".join(str(x) for x in blame_list)}],'
            ' reason is NONUNIQUE_INDEX'
        )

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
    echo '<textarea style="font-sice:small;" cols="80" rows="16" name="AXIS_SPEC_ROWS">'.$normalizedInputDataString. \
      </textarea>'."\n";
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
    echo '<table style="width:75%;"><tr><th>Laufd.Nr.</th><th>Name</th><th>Type</th><th>Min</th><th>Limit</th>\
      <th>Max</th><th>LimitFolded</th><th>MinFolded</th><th>Value</th><th>Unit</th></tr>'."\n";
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


def table(axis_maps, info_queue) -> str:
    """Display axis maps as markdown table."""
    normalized_input_data_rows = [SEMI.join(str(v) for v in axis.values()) for axis in axis_maps]
    log.debug('ReAssembledRows:')
    for row in normalized_input_data_rows:
        log.debug(row)
    normalized_input_data_string = '\n'.join(normalized_input_data_rows)
    log.debug('ReAssembledNormalizedInput:')
    log.debug(normalized_input_data_string)
    table_headers = ('ListNo.', 'Name', 'Type', 'Min', 'Limit', 'Max', 'LimitFolded', 'MinFolded', 'Value', 'Unit')
    table_header_str_row = PIPE.join(table_headers)
    table_body_str_rows = []
    for i, data in enumerate(axis_maps, start=1):
        display_row = PIPE.join(str(d) for d in data.values())
        table_body_str_rows.append(display_row)
    if info_queue:
        log.warning('InfoQueue:')
        for diagnostic in info_queue:
            log.warning(f'- {diagnostic}')
    return '\n'.join([table_header_str_row] + table_body_str_rows)
