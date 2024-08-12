from barfi import st_barfi, Block

feed = Block(name='Feed')
feed.add_output()

result = Block(name='Result')
result.add_output()
splitter = Block(name='Splitter')
splitter.add_input()
splitter.add_output()
mixer = Block(name='Mixer')
mixer.add_input()
mixer.add_input()
mixer.add_output()
st_barfi(base_blocks=[feed, result,splitter,mixer])
