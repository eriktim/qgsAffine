#!/bin/sh

version=$(cat qgsAffine/metadata.txt | sed -n 's/version=\(.*\)/\1/p')
pyVersion=$(cat qgsAffine/__init__.py | sed -n 's/.*"Version \(.*\)"/\1/p')

if [ "$version" != "$pyVersion" ]; then
  echo "The metadata and python versions do not match."
  exit 1
fi

pyrcc4 -o qgsAffine/resources.py qgsAffine/resources.qrc
pyuic4 -o qgsAffine/ui.py qgsAffine/ui.ui

dir="build"
file="$dir/qgsAffine-${version}.zip"

mkdir -p ${dir}
zip -qr ${file} qgsAffine

echo "Wrote $file"
