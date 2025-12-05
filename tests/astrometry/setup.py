import sys, os

curDir = os.path.dirname(__file__)
srcDir = os.path.abspath(os.path.join(curDir, "..", "..", "src"))
if srcDir not in sys.path:
    sys.path.append(srcDir)
os.chdir(curDir)
