qmake -tp -r -spec msvc-2019 ../qdemo.pro
PAUSE

msbuild ../qdemo.sln
PAUSE
