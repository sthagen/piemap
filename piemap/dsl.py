import json


NEEDED_NUMBER_OF_AXIS_MAX = 16
NULL_STR_REP = 'NULL'


def dumps(config):
    """Dump configuration into string."""
    return NotImplemented


def dump(config, handle):
    """Dump configuration into JSON file via handle."""
    json.dump(config, handle)


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
    return tuple(default_linear.keys())


def default_values():
    """DRY."""
    return tuple(default_linear.values())


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
        'AXIS_UNIT' => 'dB'
    }


def unsafe(text):
    """TODO(sthagen) keep/drop list applies here."""
    return text


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
        axis_values_rows_req = axis_values_rows_req_string.split()
        n_axis_rows_req = len(axis_values_rows_req)
        foreach(array_slice($axisValuesRowsReq,0,$neededNumberOfAxisMax) as $n => $rowString) {
            $axisValues = $axisDefaultValues;
            $axisValuesCand = explode(';',$rowString);
            if (count($axisValues) == count($axisValuesCand)) {
                foreach($axisValuesCand as $i => $v) {
                    if ($v != '') {
                        $axisValues[$i] = $v;
                    }
                }
            }
            $axisMap = array_combine($axisDefaultKeys,$axisValues);
            $numericAxisTypes = array('LINEAR','FOLDED');
            if($axisMap['AXIS_INDEX'] == '') {
                $axisMap['AXIS_INDEX'] = $n;
            }
            else {
                $indexCand = strval($axisMap['AXIS_INDEX']);
                $iCFC = strval(intval($indexCand));
                $axisMap['AXIS_INDEX'] = intval($iCFC);
                if ($indexCand !== $iCFC) {
                    $infoQueue[] = 'NOK \''.$indexCand.'\' index requested, accepted as \''.$iCFC.'\'';
                }
                else {
                    $infoQueue[] = ' OK \''.$indexCand.'\' index requested, accepted as \''.$iCFC.'\'';
                }
            }
            if (in_array($axisMap['AXIS_TYPE'], $numericAxisTypes)) {
                $axisMap['AXIS_MIN'] = StarPlot_minFromLimitMax($axisMap['AXIS_LIMIT'], $axisMap['AXIS_MAX']);
                if($axisMap['AXIS_VALUE'] != $nullStrRepr and !is_numeric($axisMap['AXIS_VALUE'])) {
                    $axisMap['AXIS_VALUE'] = $nullStrRepr;
                }
            }
            if ($axisMap['AXIS_TYPE'] == 'FOLDED') {
                $axisMap['AXIS_LIMIT_FOLDED'] = StarPlot_limitFoldedFromLimitMax($axisMap['AXIS_LIMIT'], $axisMap['AXIS_MAX']);
                $axisMap['AXIS_MIN_FOLDED'] = StarPlot_minFoldedFromLimitMax($axisMap['AXIS_LIMIT'], $axisMap['AXIS_MAX']);
            }
            $axisValues = array_values($axisMap);
            $someAxisMaps[] = $axisMap;
        }
        $nAxisRows = count($someAxisMaps);
        if($nAxisRowsReq > $nAxisRows) {
            $infoQueue[] = $nAxisRowsReq.' dimensions requested, but only '.$nAxisRows.' accepted. Maximum is '.$neededNumberOfAxisMax;
        }
        $bestEffortReOrderMap = array();
        $collectIndexCandList = array();
        foreach($someAxisMaps as $x => $data) {
            $indexCand = $data['AXIS_INDEX'];
            $iCFC = strval(intval($indexCand));
            $collectIndexCandList[] = $iCFC;
            if(!is_numeric($indexCand) or $iCFC != $indexCand or $indexCand < 0 or $indexCand >= $nAxisRows) {
                $hasIndexCollision = True;
                $conflictReason = 'NO_INTEGER';
                if ($iCFC != $indexCand) {
                    $conflictReason = 'DC_INTEGER';
                }
                if ($indexCand < 0) {
                    $conflictReason = 'LT_ZERO';
                }
                elseif ($indexCand >= $nAxisRows) {
                    $conflictReason = 'GT_NROW';
                }
                $infoQueue[] = 'Conflicting index rules. Failing IndexCand is '.$indexCand.', reason is '.$conflictReason;
            }
            if($indexCand != $x) {
                $hasIndexOrderMismatch = True;
                $infoQueue[] = 'Index positions not ordered. Misplaced IndexCand is '.$indexCand.', found at '.$x;
            }
            $bestEffortReOrderMap[$indexCand] = $data;
        }
        $collectIndexCandSet = array_unique($collectIndexCandList);
        if(count($collectIndexCandSet) != count($collectIndexCandList)) {
            $hasIndexCollision = True;
            $histo = array_count_values($collectIndexCandList);
            $blameList = array();
            foreach($histo as $xx => $nn) {
                if($nn != 1) {
                    $blameList[] = $xx;
                }
            }
            sort($blameList);
            $infoQueue[] = 'Conflicting index positions. Failing IndexCand/s is/are ['.implode(', ',$blameList).'], reason is '.'NONUNIQUE_INDEX';    
        }
        if(!$hasIndexCollision and $hasIndexOrderMismatch) {
            ksort($bestEffortReOrderMap);
            $someAxisMaps = array();
            foreach($bestEffortReOrderMap as $k => $data) {
                $someAxisMaps[] = $data;
            }
        }
    }
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
    return True;
}
