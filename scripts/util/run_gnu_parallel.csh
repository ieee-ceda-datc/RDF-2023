#!/usr/bin/env tcsh
set index=`date +%s`

## Update the path to the parallel executable
set parallel_exec = (/home/tool/gnu/parallel/parallel-20160822/bin/parallel)
if ( $#argv == 2 ) then
	$parallel_exec 	--joblog /tmp/SK_GNU_${index}.log \
					--bar \
					--sshloginfile $argv[2] \
					--workdir $PWD < $argv[1] 
else
	$parallel_exec 	--joblog /tmp/SK_GNU_${index}.log \
					--bar \
					-j 10 \
					--workdir $PWD < $argv[1]
endif
