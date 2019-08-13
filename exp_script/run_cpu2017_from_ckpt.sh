#!/bin/bash

############ DIRECTORY VARIABLES: MODIFY ACCORDINGLY #############
#Need to export GEM5_PATH
if [ -z ${GEM5_PATH+x} ];
then
    echo "GEM5_PATH is unset";
    exit
else
    echo "GEM5_PATH is set to '$GEM5_PATH'";
fi


#Need to export SPEC_PATH
# [mengjia] on my desktop, it is /home/mengjia/workspace/benchmarks/cpu2006
if [ -z ${SPEC_PATH+x} ];
then
    echo "SPEC_PATH is unset";
    exit
else
    echo "SPEC_PATH is set to '$SPEC_PATH'";
fi

##################################################################

ARGC=$# # Get number of arguments excluding arg0 (the script itself). Check for help message condition.
if [[ "$ARGC" != 2 ]]; then # Bad number of arguments.
    echo "run_cpu2017_from_ckpt.sh"
    echo ""
    echo "This script runs a single gem5 simulation of a single SPEC CPU2017 benchmark for x86 ISA."
    echo ""
    echo "USAGE: run_cpu2017_from_ckpt.sh <BENCHMARK> <SCHEME>"
    echo "EXAMPLE: ./run_cpu2017_from_ckpt.sh gcc UnsafeBaseline"
    echo "Schemes: UnsafeBaseline SpectreSafeInvisibleSpec FuturisticSafeInvisibleSpec"
    echo ""
    echo "A single --help help or -h argument will bring this message back."
    exit
fi

# Get command line input. We will need to check these.
BENCHMARK=$1                    # Benchmark name, e.g. bzip2
BENCHSHORT=$1                    # Benchmark name, e.g. bzip2
SCHEME=$2
######################### BENCHMARK CODENAMES ####################
PERLBENCH=600.perlbench_s
GCC=602.gcc_s
BWAVES=603.bwaves_s
MCF=605.mcf_s
CACTUSBSSN=607.cactuBSSN_s
LBM=619.lbm_s
OMNETPP=620.omnetpp_s
WRF=621.wrf_s
XALANCBMK=623.xalancbmk_s
X264=625.x264_s
CAM4=627.cam4_s
POP2=628.pop2_s
DEEPSJENG=631.deepsjeng_s
IMAGICK=638.imagick_s
LEELA=641.leela_s
NAB=644.nab_s
EXCHANGE2=648.exchange2_s
FOTONIK3D=649.fotonik3d_s
ROMS=654.roms_s
XZ=657.xz_s
##################################################################

# Check BENCHMARK input
#################### BENCHMARK CODE MAPPING ######################
if [[ "$BENCHMARK" == "perlbench" ]]; then
    BENCHMARK=$PERLBENCH
    echo $BENCHMARK
elif [[ "$BENCHMARK" == "gcc" ]]; then
    BENCHMARK=$GCC
elif [[ "$BENCHMARK" == "bwaves" ]]; then
    BENCHMARK=$BWAVES
elif [[ "$BENCHMARK" == "mcf" ]]; then
    BENCHMARK=$MCF
elif [[ "$BENCHMARK" == "cactuBSSN" ]]; then
    BENCHMARK=$CACTUSBSSN
elif [[ "$BENCHMARK" == "lbm" ]]; then
    BENCHMARK=$LBM
elif [[ "$BENCHMARK" == "omnetpp" ]]; then
    BENCHMARK=$OMNETPP
elif [[ "$BENCHMARK" == "wrf" ]]; then
    BENCHMARK=$WRF
elif [[ "$BENCHMARK" == "xalancbmk" ]]; then
    BENCHMARK=$XALANCBMK
elif [[ "$BENCHMARK" == "x264" ]]; then
    BENCHMARK=$X264
elif [[ "$BENCHMARK" == "cam4" ]]; then
    BENCHMARK=$CAM4
elif [[ "$BENCHMARK" == "pop2" ]]; then
    BENCHMARK=$POP2
elif [[ "$BENCHMARK" == "deepsjeng" ]]; then
    BENCHMARK=$DEEPSJENG
elif [[ "$BENCHMARK" == "imagick" ]]; then
    BENCHMARK=$IMAGICK
elif [[ "$BENCHMARK" == "leela" ]]; then
    BENCHMARK=$LEELA
elif [[ "$BENCHMARK" == "nab" ]]; then
    BENCHMARK=$NAB
elif [[ "$BENCHMARK" == "exchange2" ]]; then
    BENCHMARK=$EXCHANGE2
elif [[ "$BENCHMARK" == "fotonik3d" ]]; then
    BENCHMARK=$FOTONIK3D
elif [[ "$BENCHMARK" == "roms" ]]; then
    BENCHMARK=$ROMS
elif [[ "$BENCHMARK" == "xz" ]]; then
    BENCHMARK=$XZ
else
    echo "Input benchmark selection $BENCHMARK did not match any known SPEC CPU2017 benchmarks! Exiting."
    exit 1
fi

##################################################################

OUTPUT_DIR=$GEM5_PATH/m5out/cpu2017/restore/${SCHEME}/${BENCHMARK}_1_ref_x86
CKPT_OUT_DIR=$GEM5_PATH/m5out/cpu2017/ckpts/${BENCHMARK}_1_ref_x86

echo "output directory: " $OUTPUT_DIR
echo "checkpoint directory: " $CKPT_OUT_DIR

if [ -d "$OUTPUT_DIR" ]
then
    rm -r $OUTPUT_DIR
fi
mkdir -p $OUTPUT_DIR

RUN_DIR=$SPEC_PATH/run/$BENCHMARK
# Run directory for the selected SPEC benchmark
SCRIPT_OUT=$OUTPUT_DIR/runscript.log
# File log for this script's stdout henceforth

################## REPORT SCRIPT CONFIGURATION ###################

echo "Command line:"                                | tee $SCRIPT_OUT
echo "$0 $*"                                        | tee -a $SCRIPT_OUT
echo "================= Hardcoded directories ==================" | tee -a $SCRIPT_OUT
echo "GEM5_PATH:                                     $GEM5_PATH"  | tee -a $SCRIPT_OUT
echo "SPEC_PATH:                                     $SPEC_PATH"  | tee -a $SCRIPT_OUT
echo "==================== Script inputs =======================" | tee -a $SCRIPT_OUT
echo "BENCHMARK:                                    $BENCHMARK"   | tee -a $SCRIPT_OUT
echo "OUTPUT_DIR:                                   $OUTPUT_DIR"  | tee -a $SCRIPT_OUT
echo "CKPT_OUT_DIR:                                 $CKPT_OUT_DIR"| tee -a $SCRIPT_OUT
echo "==========================================================" | tee -a $SCRIPT_OUT
##################################################################


#################### LAUNCH GEM5 SIMULATION ######################
echo ""
echo "Changing to SPEC benchmark runtime directory: $RUN_DIR" | tee -a $SCRIPT_OUT
cd $RUN_DIR

echo "" | tee -a $SCRIPT_OUT
echo "" | tee -a $SCRIPT_OUT
echo "--------- Here goes nothing! Starting gem5! ------------" | tee -a $SCRIPT_OUT
echo "" | tee -a $SCRIPT_OUT
echo "" | tee -a $SCRIPT_OUT

# Actually launch gem5!
$GEM5_PATH/build/X86_MESI_Two_Level/gem5.opt \
    --outdir=$OUTPUT_DIR \
    $GEM5_PATH/configs/example/cpu2017_se.py \
    --benchmark=$BENCHSHORT \
    --benchmark-stdout=$OUTPUT_DIR/$BENCHMARK.out \
    --benchmark-stderr=$OUTPUT_DIR/$BENCHMARK.err \
    --checkpoint-dir=$CKPT_OUT_DIR \
    --checkpoint-restore=10000000000 --at-instruction \
    --maxinsts=2000000000 \
    --num-cpus=1 \
    --cpu-type=DerivO3CPU \
    --needsTSO=0 \
    --mem-size=12GB \
    --l1d_assoc=8 --l2_assoc=16 --l1i_assoc=4 \
    --ruby --num-l2caches=1 --num-dirs=1 \
    --network=garnet2.0 --topology=Mesh_XY --mesh-rows=1 \
    --scheme=$SCHEME > $SCRIPT_OUT 2>&1 &

