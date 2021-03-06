## 3.0.1
* New Features
  * None
* Bugfixes
  * Make TextReplace.TaggedReplace() non-sensitive to line ends in the text to replace
  * Make TextReplace.TaggedReplace() non-greedy (before the behavior was wrong if there were multiple instances of the tags present in the same file)

## 3.0.0
* Non-reverse compatible changes
  * Modified *\_\_init\_\_.py* to import classes without specifying their file-name.
    * Old form: *from PsiPyUtils.FileWriter import FileWriter*
    * New form: *from PsiPyUtils import FileWriter*
* New Features
  * Added packaging script and distribute as PIP package

## 2.1.0
* New Features
  * Added initial version of TextReplace module 

## 2.0.0
* First open-source release (older history discarded)
* Changes (not reverse compatible)
  * Renamed to from *Utils* to *PsiPyUtils* to avoid name clashes

## 1.2.0
* New Features
  * FileWriter: Added option to modify last line and not only remove characters with RemoveFromLastLine()
  * FileWriter: Empty lines can be written with f.WriteLn()
  * FileWriter: Optionally not overwrite existing files (exception is thrown in this case)  

## 1.1.1
* Bugfixes
  * ExtAppCall blocked under some circumstances (subprocess communication did not work propperly). Fixed this by using files to communicate (this seems the only OS independent mechanism that works reliably)

## 1.1.0
* New Features
  * Added file operations with wildcards (OpenWithWildcard, FindWithWildcard, RemoveWithWildcard)
  * Added AbsPathLinuxStyle (get absolute path in Linux style, also on Windows PCs)
* Bugfixes
  * Made ExtAppCall working on Unix Systems (failed because shell=True was missing at one place)

## V1.00
* First release