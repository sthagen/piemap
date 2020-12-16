# python-piemap
One-view visualization of grouped characterizations 

## Status
Prototyping.

## From HowTo of Reference Implementation:
>* The tool uses a simple text area (shown below), to accept lines of semicolon-separated entries of data (point or comma are both accepted as floating point separators for all numeric input values).
>* The general format for data lines is:
>  AXIS_NO;AXIS_NAME;AXIS_TYPE;MIN;LIMIT;MAX;VALUE;UNIT where usually only LIMIT, MAX and VALUE must be set. 
> Thus a minimal valid input data set could be a one liner like: ;;;;1;2;0.8; producing one full circle sector not quite reaching the limit.
>* The sectors are plotted clockwise starting at 12:00 in the sequence the lines of data are input. The first entry of each line may override this by explicitly setting this number (starting at 0).
>* The default axis type is LINEAR. Other types like FOLDED, CATEGORIAL or BIMONOTONE have to be requested by entering the respective keyword into the third column of the data line.
>* The axis types LINEAR, FOLDED and CATEGORIAL result in scaling the area (CATEGORIAL equally spaced), whereas the axis type BIMONOTONE is scaled linear with respect to the radius.
>* The axis type ORDER may be used to introduce ordered categorial scales (based on a declaration of the set of ordered values):
>    1. Declaration: ORDER_DT;DUMMY;2c;2b;2a;1 eg. for doubletalk type. The lowest (leftmost value) will be placed at the origin of the segment. 
>       An axis definition might then be: ;DT Type;ORDER_DT;;2b;1;2c;
>    2. Declaration: ORDER_LC;ORIGIN;not ok;LIMIT_VALUE;ok eg. for "Live Call". The (never occurring) placeholder LIMIT_VALUE will be placed at the limit of the segment.
>* The axis type BIMONOTONE scales linear (in the radius, not the area) from Origin to Limit and from Limit to Outer circle and thus needs declaration of a Value corresponding to the origin.
>* A title can be set by adding a line like eg. SHOW_TITLE;A long title for the plot
>* For the picture title and for the segment labeling, a pipe symbol, i.e. "|" will cause a line break.
>* The display of the values reached may be enabled by adding a line like eg. SHOW_VALUE;1
>* The display of the units may be disabled by adding a line like eg. SHOW_UNIT;0
>* Appending a SHOW_abc to an axis definition line, toggles the state of the global definition of SHOW_abc.
>* The default coloring may be changed by adding a line like eg. COLORING_DEFAULT;#FFFFFF;#DD0000;#FFFF20;#008800 or amended by adding a line like eg. COLORING_OPTIONAL;#FFFFFF;#FF2020;#FFFF20;#77FF20. 
>  The keyword COLORING_DEFAULT is magic and used for each axis per default. The entries following the COLORING* keyword are hexadecimal RGB values with # as prefix and are mapped onto NULL, MIN, LIMIT, MAX. Non-matching inputs are rewritten as #FFFFFF. 
>   If another coloring scheme shall be used per axis, this must be declared as additional entry in the axis declaration following the usual entries by referencing the relevant coloring label, eg. ;;;;1;2;0.8;;COLORING_OPTIONAL.
>* By pressing the button “Parse and plot” you will get the result in the right hand area(s) if your browser has session cookies enabled

**Note**: The name of the default branch is `default`.
