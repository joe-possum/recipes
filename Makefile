INSTALL_DIR = /usr/local/bin
NAME_PREFIX = ${shell python3 net-weight.py --name-prefix}
VESSELS = ${shell python3  net-weight.py --list}
TARGETS = ${foreach target,${VESSELS},${INSTALL_DIR}/${NAME_PREFIX}-${target}}

default :
	echo TARGETS=${TARGETS}

install :
	install -d -m 0755 ${INSTALL_DIR}
	echo '#! /usr/bin/env python3' | cat - net-weight.py > ${INSTALL_DIR}/${NAME_PREFIX}
	chmod 0755 ${INSTALL_DIR}/${NAME_PREFIX}
	rm -f ${TARGETS}
	${foreach target,${TARGETS},ln -s ${NAME_PREFIX} ${target} ; }

