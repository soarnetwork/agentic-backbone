@echo off
setlocal
set SPHINXBUILD=sphinx-build
set SOURCEDIR=source
set BUILDDIR=build

if "%1"=="" goto help

if "%1"=="clean" (
    if exist %BUILDDIR% rd /s /q %BUILDDIR%
    goto end
)

if "%1"=="html" (
    %SPHINXBUILD% -b html %SOURCEDIR% %BUILDDIR%\html
    echo Build finished. The HTML pages are in %BUILDDIR%\html.
    goto end
)

echo Unknown target: %1
goto help

:help
echo Please use 'make.bat <target>' where <target> is one of
echo   clean  - remove built documentation
echo   html   - build HTML documentation

:end
