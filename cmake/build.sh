
WORK_DIR=work

function run_build()
{
	
	mkdir $WORK_DIR
	cd $WORK_DIR
	
	cmake ../ -DCMAKE_INSTALL_PREFIX=../
	make -j 2
	make install
}

if [ "$1" == "clean" ]; then
	rm -rf $WORK_DIR
else
	run_build
fi

