import sys

EXAMPLE_APPLICATION_BINARY = "/Users/endeavor/code/complexity/example0"
BINARY_NINJA_API_PATH = "/Applications/Binary Ninja.app/Contents/Resources/python"
BINARY_NINJA_PLUGINS_PATH = "/Users/endeavor/Library/Application Support/Binary Ninja/plugins"

sys.path.append(BINARY_NINJA_API_PATH)
sys.path.append(BINARY_NINJA_PLUGINS_PATH)

from binaryninja import *
import varslice

bv = BinaryViewType.get_view_of_file(EXAMPLE_APPLICATION_BINARY)

bb = bv.get_basic_blocks_at(0x100000f2e)[0]

graph = varslice.graph_function(bb.function)

dominators = graph.compute_dominators()

for index in dominators :
    print hex(index), map(lambda x: hex(x), dominators[index])