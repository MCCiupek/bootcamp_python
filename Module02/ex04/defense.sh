# Correction:
cd ..
rm -rf tmp_env
python3 -m venv tmp_env
source tmp_env/bin/activate
pip list
cd ex04/ && bash build.sh
ls dist
pip list
pip show -v my_minipack
deactivate