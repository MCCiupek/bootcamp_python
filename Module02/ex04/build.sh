WHL=./dist/my_minipack-1.0.0-py3-none-any.whl
TAR=./dist/my_minipack-1.0.0.tar.gz

# Upgrade packages
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade wheel

# Wheel
python setup.py bdist_wheel --universal
mv ./dist/my_minipack-1.0.0-py2.py3-none-any.whl "$WHL"
if [ -f "$WHL" ]; then
    pip install "$WHL"
else
    echo "File not found: $WHL"
fi

# Tar
# rm -rf dist && mkdir dist
tar -czf "$TAR" .
if [ -f "$TAR" ]; then
    pip install "$TAR"
else
    echo "File not found: $TAR"
fi
