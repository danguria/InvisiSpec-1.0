import m5
from m5.objects import *

# 600.perlbench_s
perlbench = Process() # Update June 7, 2017: This used to be LiveProcess()
perlbench.executable =  '../../bin/600.perlbench_s'
args = ['-I./lib', 'checkspam.pl', '2500', '5', '25', '11', '150', '1', '1',
        '1', '1']
# Ref command
perlbench.cmd = [perlbench.executable] + args
perlbench.output = 'checkspam.2500.5.25.11.150.1.1.1.1.out'
perlbench.errout = 'checkspam.2500.5.25.11.150.1.1.1.1.err'

# 602.gcc_s
gcc = Process()
gcc.executable = '../../bin/602.gcc_s'
args = ['gcc-pp.c', '-O5', '-fipa-pta', '-o', 'gcc-pp.opts-O5_-fipa-pta.s']
# Ref command
gcc.cmd = [gcc.executable] + args
gcc.output = 'gcc-pp.opts-O5_-fipa-pta.out'
gcc.errout = 'gcc-pp.opts-O5_-fipa-pta.err'

# 603.bwaves_s
bwaves = Process()
bwaves.executable = '../../bin/603.bwaves_s'
bwaves.cmd = [bwaves.executable] + ['bwaves_1']
bwaves.input = 'bwaves_1.in'
bwaves.output = 'bwaves_1.out'
bwaves.errout = 'bwaves_1.err'

# 605.mcf_s
mcf = Process()
mcf.executable = '../../bin/605.mcf_s'
mcf.cmd = [mcf.executable] + ['inp.in']
mcf.output = 'inp.out'
mcf.errout = 'inp.err'

# 607.cactuBSSN_s
cactuBSSN = Process()
cactuBSSN.executable = '../../bin/607.cactuBSSN_s'
cactuBSSN.cmd = [cactuBSSN.executable] + ['spec_ref.par']
cactuBSSN.output = 'spec_ref.out'
cactuBSSN.errout = 'spec_ref.err'

# 619.lbm_s
lbm = Process()
lbm.executable = '../../bin/619.lbm_s'
args = ['2000', 'reference.dat', '0', '0', '200_200_260_ldc.of']
lbm.cmd = [lbm.executable] + args
lbm.output = 'lbm.out'
lbm.errout = 'lbm.err'

# 620.omnetpp_s
omnetpp = Process()
omnetpp.executable = '../../bin/620.omnetpp_s'
omnetpp.cmd = [omnetpp.executable] + ['-c', 'General', '-r', '0']
omnetpp.output = 'omnetpp.General-0.out'
omnetpp.errout = 'omnetpp.General-0.err'

# 621.wrf_s
wrf = Process()
wrf.executable = '../../bin/621.wrf_s'
wrf.cmd = [wrf.executable]
wrf.output = 'rsl.out.0000'
wrf.errout = 'wrf.err'

# 623.xalancbmk_s
xalancbmk = Process()
xalancbmk.executable = '../../bin/623.xalancbmk_s'
xalancbmk.cmd = [xalancbmk.executable] + ['-v', 't5.xml', 'xalanc.xsl']
xalancbmk.output = 'ref-t5.out'
xalancbmk.errout = 'ref-t5.err'

# 625.x264_s
x264 = Process()
x264.executable = '../../bin/625.x264_s'
args = ['--seek', '500', '--dumpyuv', '200', '--frames', '1250', '-o',
        'BuckBunny_New.264', 'BuckBunny.yuv', '1280x720']
x264.cmd = [x264.executable] + args
x264.output = 'run_0500-1250_x264_s.out'
x264.errout = 'run_0500-1250_x264_s.err'

# 627.cam4_s
cam4 = Process()
cam4.executable = '../../bin/627.cam4_s'
cam4.cmd = [cam4.executable]
cam4.output = 'cam4_s.out'
cam4.errout = 'cam4_s.err'

# 628.pop2_s
pop2 = Process()
pop2.executable = '../../bin/628.pop2_s'
pop2.cmd = [pop2.executable]
pop2.output = 'pop2_s.out'
pop2.errout = 'pop2_s.err'

# 631.deepsjeng_s
deepsjeng = Process()
deepsjeng.executable = '../../bin/631.deepsjeng_s'
deepsjeng.cmd = [deepsjeng.executable] + ['ref.txt']
deepsjeng.output = 'ref.out'
deepsjeng.errout = 'ref.err'

# 638.imagick_s
imagick = Process()
imagick.executable = '../../bin/638.imagick_s'
args = ['-limit', 'disk', '0', 'refspeed_input.tga', '-resize', '817%',
        '-rotate', '-2.76', '-shave', '540x375', '-alpha', 'remove',
        '-auto-level', '-contrast-stretch', '1x1%', '-colorspace', 'Lab',
        '-channel', 'R', '-equalize', '+channel', '-colorspace', 'sRGB',
        '-define', 'histogram:unique-colors=false', '-adaptive-blur', '0x5',
        '-despeckle', '-auto-gamma', '-adaptive-sharpen', '55', '-enhance',
        '-brightness-contrast', '10x10', '-resize', '30%',
        'refspeed_output.tga']
imagick.cmd = [imagick.executable] + args
imagick.output = 'refspeed_convert.out'
imagick.errout = 'refspeed_convert.err'

# 641.leela_s
leela = Process()
leela.executable = '../../bin/641.leela_s'
leela.cmd = [leela.executable] + ['ref.sgf']
leela.output = 'ref.out'
leela.errout = 'ref.err'

# 644.nab_s
nab = Process()
nab.executable = '../../bin/644.nab_s'
nab.cmd = [nab.executable] + ['3j1n', '20140317', '220']
nab.output = '3j1n.out'
nab.errout = '3j1n.err'

# 648.exchange2_s
exchange2 = Process()
exchange2.executable = '../../bin/648.exchange2_s'
exchange2.cmd = [exchange2.executable] + ['6']
exchange2.output = 'exchange2.txt'
exchange2.errout = 'exchange2.err'

# 649.fotonik3d_s
fotonik3d = Process()
fotonik3d.executable = '../../bin/649.fotonik3d_s'
fotonik3d.cmd = [fotonik3d.executable]
fotonik3d.output = 'fotonik3d_s.log'
fotonik3d.errout = 'fotonik3d_s.err'

# 654.roms_s
roms = Process()
roms.executable = '../../bin/654.roms_s'
roms.cmd = [roms.executable]
roms.input = 'ocean_benchmark3.in'
roms.output = 'ocean_benchmark3.log'
roms.errout = 'ocean_benchmark3.err'

# 657.xz_s
xz = Process()
xz.executable = '../../bin/657.xz_s'
string = '055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d971\
        3be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae'
args = ['cpu2006docs.tar.xz', '6643', string, '1036078272', '1111795472', '4']
xz.cmd = [xz.executable] + args
xz.output = 'cpu2006docs.tar-6643-4.out'
xz.errout = 'cpu2006docs.tar-6643-4.err'

# 996.specrand_fs
specrand_f = Process()
specrand_f.executable = '../../bin/996.specrand_fs'
specrand_f.cmd = [specrand_f.executable] + ['1255432124', '234923']
specrand_f.output = 'rand.234923.out'
specrand_f.errout = 'rand.234923.err'

# 998.specrand_is
specrand_i = Process()
specrand_i.executable = '../../bin/998.specrand_is'
specrand_i.cmd = [specrand_i.executable] + ['1255432124', '234923']
specrand_i.output = 'rand.234923.out'
specrand_i.errout = 'rand.234923.err'
