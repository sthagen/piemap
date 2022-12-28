# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/piemap/blob/default/sbom.json) with SHA256 checksum ([132e8714 ...](https://git.sr.ht/~sthagen/piemap/blob/default/sbom.json.sha256 "sha256:132e87146535996857a8c2e3e5be26be16c769ece206bae20ecaa188ecddcf1b")).
<!--[[[end]]] (checksum: 9e873a3516175358c3a54808b62616cf)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                       | Version                                         | License                                            | Author                       | Description (from packaging data)                                  |
|:-------------------------------------------|:------------------------------------------------|:---------------------------------------------------|:-----------------------------|:-------------------------------------------------------------------|
| [Pillow](https://python-pillow.org)        | [9.3.0](https://pypi.org/project/Pillow/9.3.0/) | Historical Permission Notice and Disclaimer (HPND) | Alex Clark (PIL Fork Author) | Python Imaging Library (Fork)                                      |
| [typer](https://github.com/tiangolo/typer) | [0.7.0](https://pypi.org/project/typer/0.7.0/)  | MIT License                                        | Sebastián Ramírez            | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: 8ab7b6be4e89689e746866df58cd10dd)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                          | Version                                        | License     | Author         | Description (from packaging data)         |
|:----------------------------------------------|:-----------------------------------------------|:------------|:---------------|:------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.3](https://pypi.org/project/click/8.1.3/) | BSD License | Armin Ronacher | Composable command line interface toolkit |
<!--[[[end]]] (checksum: dc3a866a7aa3332404bde3da87727cb9)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
Pillow==9.3.0
typer==0.7.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 6e3238f53f3eccd38fc22f50384abd5c)-->
