# piemap

One-view visualization of grouped characterizations (Quality Pie).

[License: MIT](https://git.sr.ht/~sthagen/piemap/tree/default/item/LICENSE)

[![version](https://img.shields.io/pypi/v/piemap.svg?style=flat)](https://pypi.python.org/pypi/piemap/)
[![downloads](https://pepy.tech/badge/piemap/month)](https://pepy.tech/project/piemap)
[![wheel](https://img.shields.io/pypi/wheel/piemap.svg?style=flat)](https://pypi.python.org/pypi/piemap/)
[![supported-versions](https://img.shields.io/pypi/pyversions/piemap.svg?style=flat)](https://pypi.python.org/pypi/piemap/)
[![supported-implementations](https://img.shields.io/pypi/implementation/piemap.svg?style=flat)](https://pypi.python.org/pypi/piemap/)

## Documentation

User and developer [documentation of piemap](https://codes.dilettant.life/docs/piemap).

## Bug Tracker

Feature requests and bug reports are best entered in the [todos of piemap](https://todo.sr.ht/~sthagen/piemap).

## Primary Source repository

The primary source of `piemap` lives somewhere on a mountain in Central Switzerland.
But, we use decentralized version control (git), so any clone can become the source to everyone's benefit, no central only code.
Anyway, the preferred public clones of `piemap` are:

* [on codeberg](https://codeberg.org/sthagen/piemap) - a democratic community-driven, non-profit software development platform operated by Codeberg e.V.
* [at sourcehut](https://git.sr.ht/~sthagen/piemap) - a collection of tools useful for software development.

## Status

Experimental

## Short How to Quality Pie

*(From HowTo of Reference Implementation)*

* The tool uses a simple text area (shown below), to accept lines of semicolon-separated entries of data (point or comma are both accepted as floating point separators for all numeric input values).
* The general format for data lines is:
  AXIS_NO;AXIS_NAME;AXIS_TYPE;MIN;LIMIT;MAX;VALUE;UNIT where usually only LIMIT, MAX and VALUE must be set. 
 Thus a minimal valid input data set could be a one liner like: ;;;;1;2;0.8; producing one full circle sector not quite reaching the limit.

* The sectors are plotted clockwise starting at 12:00 in the sequence the lines of data are input. The first entry of each line may override this by explicitly setting this number (starting at 0).

* The default axis type is LINEAR. Other types like FOLDED, CATEGORIAL or BIMONOTONE have to be requested by entering the respective keyword into the third column of the data line.

* The axis types LINEAR, FOLDED and CATEGORIAL result in scaling the area (CATEGORIAL equally spaced), whereas the axis type BIMONOTONE is scaled linear with respect to the radius.

* The axis type ORDER may be used to introduce ordered categorial scales (based on a declaration of the set of ordered values):
    1. Declaration: ORDER_DT;DUMMY;2c;2b;2a;1 eg. for doubletalk type. The lowest (leftmost value) will be placed at the origin of the segment. 
       An axis definition might then be: ;DT Type;ORDER_DT;;2b;1;2c;
    2. Declaration: ORDER_LC;ORIGIN;not ok;LIMIT_VALUE;ok eg. for "Live Call". The (never occurring) placeholder LIMIT_VALUE will be placed at the limit of the segment.

* The axis type BIMONOTONE scales linear (in the radius, not the area) from Origin to Limit and from Limit to Outer circle and thus needs declaration of a Value corresponding to the origin.

* A title can be set by adding a line like eg. SHOW_TITLE;A long title for the plot
* For the picture title and for the segment labeling, a pipe symbol, i.e. "|" will cause a line break.
* The display of the values reached may be enabled by adding a line like eg. SHOW_VALUE;1
* The display of the units may be disabled by adding a line like eg. SHOW_UNIT;0
* Appending a SHOW_abc to an axis definition line, toggles the state of the global definition of SHOW_abc.
* The default coloring may be changed by adding a line like eg. COLORING_DEFAULT;#FFFFFF;#DD0000;#FFFF20;#008800 or amended by adding a line like eg. COLORING_OPTIONAL;#FFFFFF;#FF2020;#FFFF20;#77FF20. 
  The keyword COLORING_DEFAULT is magic and used for each axis per default. The entries following the COLORING* keyword are hexadecimal RGB values with # as prefix and are mapped onto NULL, MIN, LIMIT, MAX. Non-matching inputs are rewritten as #FFFFFF. 
   If another coloring scheme shall be used per axis, this must be declared as additional entry in the axis declaration following the usual entries by referencing the relevant coloring label, eg. ;;;;1;2;0.8;;COLORING_OPTIONAL.

* By pressing the button “Parse and plot” you will get the result in the right hand area(s) if your browser has session cookies enabled

## ... as in ITU-T P.505

*(Informational text of Reference Implementation)*

### Preface

The numerous complex parameters that determine the quality of telecommunication equipment as well as end-to-end quality can be interpreted by technical experts only.

This tool provides a novel quality representation methodology which is easy to use and also easy to understand for non-experts and which can serve as a basis for commercial decisions on a management or marketing level with

* Quick and easy recognition of expected speech quality problems for selected parameters (limit value violation);
* Assessment of strengths and weaknesses of signal processing implemented in a terminal or other telecommunication equipment, including end-to-end considerations (quality statement);
* Easy comparison of different equipment or connections based on the corresponding representations;
* Easy extension of the representation by new parameters relevant to quality in the future.

### Introduction

The one-view visualization methodology is based on the allocation of individual circle segments to the selected parameters - the so-called "quality pie"; a maximum number of 16 different segments is considered here for practical reasons.

The total number of parameters represented determines the size of the individual segments in the quality pie. The axes are shown with a common origin. The individual circle segments have the same size (spanned angle 360° divided by number of selected quality parameters).

The representation of individual segment sizes is not interdependent, thus guaranteeing the independence of the different quality parameters from each other, which leads to the following advantages:

* Independent representation of individual quality parameters.
* Segment sizes are determined by the number of selected parameters and are identical.
* Segment size (radius) is a measure for the quality regarding this parameter.
* A concentric circle around the origin is defined (1/√2) which represents a minimum quality measure; falling below this segment size (radius) indicates a non-compliance with this limit value.
* By means of a suitable colour selection results lying within the tolerance or transgressing the limit values can be easily visualized.

This online application of P.505 can help you to produce high quality graphs for your individual set of parameters. It is intended to support the use of this methodology in the field, e.g. for recurring reporting task, but also for benchmarking or for test events.

### Types of axes

The advantage of this tool is the ability to use different types of axes (scalings) within one quality pie, depending on your needs. There are four different types of axes. It is very important to first of all select the right type of axis for each parameter you want to display. The types itself are explained below, whereas the application of them is explained under ‘operating the tool’.

#### LINEAR

The linear axis type is scaling the area, based on the input values for minimum, limit and maximum.

The minimum value cannot be specified, it will be determined by continuing the scale defined by limit and maximum values. Any entries in the MIN section will be ignored.

#### FOLDED

The folded axis type is scaling the area and (quite similar to the linear axis type) with the important exception that this scale is literally folded.

The maximum value is not a numerical maximum but rather an optimum, for the limit there will be two values, i.e.:

1.) LIMIT
2.) 2×MAX - LIMIT

The minimum value will be determined in the same way as for the linear scale, i.e. any entries in the MIN section will be ignored and both the scale ends will be calculated as predefined by the limit and maximum values.

#### BI-MONOTONE

The axis type BI-MONOTONE scales linear (in the radius, not the area) from the origin to the limit and from the limit to the maximum.

It therefore requires the input of a minimum value. The scales in both segments of the axis can be as much different as desired.

#### CATEGORIAL

The categorial axis type is scaling the area, equally spaced, and can be used to display results, which are achieved without a scale.

For the data input lines this type is also referred to as ORDER*. The axis type ORDER* may be used to introduce ordered categorical scales (based on a declaration of the set of ordered values), see the following two examples:

1.) Declaration: ORDER_DT;DUMMY;2c;2b;2a;1 e.g. for doubletalk type.

The placeholder "DUMMY" is used to initiate the axis at the origin of the segment.

An axis definition might then be: ;DT Type;ORDER_DT;;2b;1;2c;

2.) Declaration: ORDER_LC;ORIGIN;not ok;LIMIT_VALUE;ok e.g. for "Live Call".

The placeholder "ORIGIN" is used to initiate the axis at the origin of the segment, whereas the placeholder "LIMIT_VALUE" is used to define the axis across the limit circle of the segment.

Other ordered categorial scales can be defined as needed, but care has to be taken that the categories can be ordered in the same dimension; e.g.:

* "Very Good, Good, Fair, Poor, Bad" can be ordered with sense;
* "Loud, Good, Noisy, Poor" cannot be ordered because different dimensions are used.

### Operating the tool

The composition of the data input lines is done in the text box on the left side of the browser window.

The separation of commands within one line is done by semicolon (;). For many parameters no entry renders a default value. Both, point (.) and comma (,) are accepted as decimal separator.

There are separate data input lines for labelling of the quality pie and it segments. You can select a title for the plot and decide whether values and units should be displayed along with the segments.

For practical reasons you import and export your settings and values to and from your own excel spreadsheet(s). As a starting point it might useful to export the default quality pie from the website into an excel spreadsheet and start working from there on.

The "Template" tab contains the set of data input lines, which will produce the quality pies as contained in P.505. They can be used as a good starting point to derive easily similar quality pies.

The sectors are plotted clockwise starting at 12:00 in the sequence the data input lines are listed.

The general format for data input lines creating segments is:

AXIS_NO;AXIS_NAME;AXIS_TYPE;MIN;LIMIT;MAX;VALUE;UNIT where usually only LIMIT, MAX and VALUE must be set.

These data input lines have to be written for each segment that should be created. Below the data input field buttons are placed which assist to create data input lines corresponding to the four different types of axes.

#### AXIS_NO

This entry means axis number, which by default is the consecutive number in the order of the segment command lines. Thus switching the segment command lines will result in switching the segments in the quality pie, unless explicitly numbered (starting at 0).

#### AXIS_NAME

This entry can be used to display the name of the parameter next to the outer end of the segment, if not switched off by a global setting.

#### AXIS_TYPE

This entry can be used to select the type of axis as explained above; the default setting is LINEAR.

#### MIN

The minimum value of the axis; for linear and folded scales any entries in this section will be ignored; the categorial scale does also not make direct use of minimum values.

#### LIMIT

Limit between result values considered ok and result values considered not ok. In the case of the FOLDED axis type, there will be two values displayed:

1.) LIMIT

2.) 2×MAX - LIMIT

#### MAX

Maximum or optimum value of the axis that can be reached for this parameter.

#### VALUE

Actually achieved result value for each parameter; this determines the actual size of the coloured areas; the display of the value itself next to the outer end of the segment can be enabled by a global setting.

#### UNIT

This entry can be used to add a unit to the result value, if not disabled by a global setting.

A pipe symbol, i.e. "|" will cause a line break.

#### Global data input lines affecting the entire pie chart are

For the picture title and for the segment labelling, a pipe symbol, i.e. "|" will cause a line break.

A title for the pie chart can be set by adding a line like e.g. SHOW_TITLE;A long title for the plot.

The display of the result values achieved may be enabled by adding a line like e.g. SHOW_VALUE;1.

The display of the units may be disabled by adding a line like e.g. SHOW_UNIT;0.

Appending a SHOW* to an axis definition line, toggles the state of the global definition of SHOW*; where * can be UNIT or TITLE.

The default coloring may be changed by adding a line like e.g. COLORING_DEFAULT;#FFFFFF;#DD0000;#FFFF20;#008800.

The entries following the COLORING* keyword are hexadecimal RGB values with # as prefix and are mapped onto NULL, MIN, LIMIT, MAX. Non-matching inputs are rewritten as #FFFFFF.

If different coloring schemes should be used per axis, they must be declared as additional entries in the data input lines appended to the general format, explained above, and referring to the relevant coloring label, e.g. ;;;;1;2;0.8;;COLORING*.

Of course, such COLORING* settings should be defined before they can be referred to, e.g.

COLORING_Eagle;#FFFFFF;#FF2020;#FFFF20;#77FF20.

#### Resulting Pie Chart

By pressing the button “Parse and plot” the resulting pie chart will be displayed in the right hand area(s) if your browser has session cookies enabled.

Depending on your browser settings, display etc., some details may not be displayed as expected; click onto the pie chart to see the original (i.e. larger) picture, which should be ok.

The input data lines together with the quality pie can be exported to Excel or the graph can be saved in jpg or png format, respectively.

### Parameters

Examples of speech quality parameters together with typical values are to be found in Recommendation ITU-T P.505.

However, the application of this tool is not limited to such parameters. In general, any kind of quality related parameters can be used. However, it is recommended to carefully select a set of parameters which is reflecting all aspects of the quality for the topic or device under consideration, e.g.: selecting only parameters with respect to the receiving channel might not be a balanced decision when attempting to benchmark mobile telephone sets.

**Note**: The default branch is `default`.
