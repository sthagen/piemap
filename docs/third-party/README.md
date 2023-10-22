# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/piemap/blob/default/sbom/cdx.json) with SHA256 checksum ([8327d42e ...](https://git.sr.ht/~sthagen/piemap/blob/default/sbom/cdx.json.sha256 "sha256:8327d42ec1a8c8bdb990643172182eb0839e3c6b38f4ce038ab7c73216222f11")).
<!--[[[end]]] (checksum: 73837e5f1efe453a1272d1ff400b4dfa)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                       | Version                                           | License                                            | Author                  | Description (from packaging data)                                  |
|:-------------------------------------------|:--------------------------------------------------|:---------------------------------------------------|:------------------------|:-------------------------------------------------------------------|
| [Pillow](https://python-pillow.org)        | [10.1.0](https://pypi.org/project/Pillow/10.1.0/) | Historical Permission Notice and Disclaimer (HPND) | Jeffrey A. Clark (Alex) | Python Imaging Library (Fork)                                      |
| [typer](https://github.com/tiangolo/typer) | [0.9.0](https://pypi.org/project/typer/0.9.0/)    | MIT License                                        | Sebastián Ramírez       | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: c89c6e6e30509348a4b21dca72f06f3c)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                          | Version                                        | License     | Author                                | Description (from packaging data)         |
|:----------------------------------------------|:-----------------------------------------------|:------------|:--------------------------------------|:------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.6](https://pypi.org/project/click/8.1.6/) | BSD License | Pallets <contact@palletsprojects.com> | Composable command line interface toolkit |
<!--[[[end]]] (checksum: 7b69d9be7fa227d2db394dcd865606d8)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
Pillow==10.1.0
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.6]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: 3afc955f3c8575f3fd85f144f602b971)-->
