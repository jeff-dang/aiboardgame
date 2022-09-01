# Makefile
# TODO: Missing artifacts should be added to this file
.PHONY:	SRS

all:	SRS MG MIS PS VnVP VnVR

SRS:
	cd SRS && make && cd ..

MG:
	cd Design/MG && make && cd ../..

MIS:
	cd Design/MIS && make && cd ../..

PS:
	cd ProblemStatement && make && cd ..

VnVP:
	cd VnVPlan && make && cd ../..

VnVR:
	cd VnVReport && make && cd ../..


clean:	cleanSRS cleanMG cleanMIS cleanPS cleanVnVP cleanVnVR

cleanPS:
	cd ProblemStatement && make clean && cd ..

cleanSRS:
	cd SRS && make clean && cd ..

cleanMG:
	cd Design/MG && make clean && cd ..

cleanMIS:
	cd Design/MIS && make clean && cd ..

cleanVnVP:
	cd VnVPlan && make clean && cd ..

cleanVnVR:
	cd VnVReport && make clean && cd ..
