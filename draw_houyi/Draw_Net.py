
import sys
sys.path.append(r'C:\Users\lyfhouyi\Desktop\git\plot-network')
sys.path.append(r'C:\Users\Monkey.E\Desktop\git\plot-network')
from pycore.tikzeng import *

def draw_Net4():
    arch = [
        to_head( '..' ),
        to_cor(),
        to_begin(),

        # 第一帧
        to_Conv("input", 32, 96,3, offset="(0,0,0)", to="(0,0,0)", height=32, depth=96, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=18, height=6),
        
        to_ConvRelu("conv1", 28, 82,6, offset="(3,0,0)", to="(input-east)", height=28, depth=82, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 40,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=40, width=6,caption="MaxPool"),
            
        to_ConvRelu("conv2", 10, 26,8, offset="(3,0,0)", to="(pool1-east)", height=10, depth=26, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool2", 5, 12,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=12, width=8,caption="MaxPool"),
        
        to_ConvRelu("conv3", 5, 12,8, offset="(2,0,0)", to="(pool2-east)", height=5, depth=12, width=8,caption='conv3'),
        to_connection( "pool2", "conv3"), 
        to_Pool("pool31", 2, 4,8,offset="(0,0,0)", to="(conv3-east)",height=2, depth=4, width=8,caption="MaxPool"),
        
        # 第二帧
        to_Conv("input", 32, 96,3, offset="(0,15,0)", to="(0,0,0)", height=32, depth=96, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=18, height=6),
        
        to_ConvRelu("conv1", 28, 82,6, offset="(3,0,0)", to="(input-east)", height=28, depth=82, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 40,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=40, width=6,caption="MaxPool"),
            
        to_ConvRelu("conv2", 10, 26,8, offset="(3,0,0)", to="(pool1-east)", height=10, depth=26, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool2", 5, 12,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=12, width=8,caption="MaxPool"),
        
        to_ConvRelu("conv3", 5, 12,8, offset="(2,0,0)", to="(pool2-east)", height=5, depth=12, width=8,caption='conv3'),
        to_connection( "pool2", "conv3"), 
        to_Pool("pool32", 2, 4,8,offset="(0,0,0)", to="(conv3-east)",height=2, depth=4, width=8,caption="MaxPool"),

        # 第三帧
        to_Conv("input", 32, 96,3, offset="(0,30,0)", to="(0,0,0)", height=32, depth=96, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=18, height=6),
        
        to_ConvRelu("conv1", 28, 82,6, offset="(3,0,0)", to="(input-east)", height=28, depth=82, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 40,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=40, width=6,caption="MaxPool"),
            
        to_ConvRelu("conv2", 10, 26,8, offset="(3,0,0)", to="(pool1-east)", height=10, depth=26, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool2", 5, 12,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=12, width=8,caption="MaxPool"),
        
        to_ConvRelu("conv3", 5, 12,8, offset="(2,0,0)", to="(pool2-east)", height=5, depth=12, width=8,caption='conv3'),
        to_connection( "pool2", "conv3"), 
        to_Pool("pool33", 2, 4,8,offset="(0,0,0)", to="(conv3-east)",height=2, depth=4, width=8,caption="MaxPool"),

        # 第四帧
        to_Conv("input", 32, 96,3, offset="(0,45,0)", to="(0,0,0)", height=32, depth=96, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=18, height=6),
        
        to_ConvRelu("conv1", 28, 82,6, offset="(3,0,0)", to="(input-east)", height=28, depth=82, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 40,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=40, width=6,caption="MaxPool"),
            
        to_ConvRelu("conv2", 10, 26,8, offset="(3,0,0)", to="(pool1-east)", height=10, depth=26, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool2", 5, 12,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=12, width=8,caption="MaxPool"),
        
        to_ConvRelu("conv3", 5, 12,8, offset="(2,0,0)", to="(pool2-east)", height=5, depth=12, width=8,caption='conv3'),
        to_connection( "pool2", "conv3"), 
        to_Pool("pool34", 2, 4,8,offset="(0,0,0)", to="(conv3-east)",height=2, depth=4, width=8,caption="MaxPool"),

        # 全连接层
        to_Sum( "sum", offset="(12,7,0)", to="(pool32-east)", radius=2.5, opacity=0.6),
        to_connection( "pool31", "sum"),
        to_connection( "pool32", "sum"),
        to_connection( "pool33", "sum"),
        to_connection( "pool34", "sum"),

        to_Cascade("cascade", 1, 256,1, offset="(5,0,0)", to="(sum-east)", height=3.5, depth=256, width=3.5,caption='cascade'),
        to_connection( "sum", "cascade"), 

        to_FcRelu_fine("fc1", 1, 32,1, offset="(3,0,0)", to="(cascade-east)", height=2.5, depth=32, width=2.5,caption='fc1'),
        to_connection( "cascade", "fc1"), 
        
        to_SoftMax("softMax", 1 ,4,1, offset="(3,0,0)", to="(fc1-east)", height=1, depth=4, width=1, caption="SoftMax"  ),
        to_connection( "fc1", "softMax"), 

        to_end()
        ]
    to_generate(arch, os.getcwd()+'\\draw_houyi\\Net4\\Net4.tex' )
    # end draw_Net4


def draw_Net42():
    arch = [
        to_head( '..' ),
        to_cor(),
        to_begin(),

        # 第一帧
        to_Conv("input", 32, 32,3, offset="(0,0,0)", to="(0,0,0)", height=32, depth=32, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=6, height=6),
        
        to_ConvRelu("conv1", 28, 28,6, offset="(3,0,0)", to="(input-east)", height=28, depth=28, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 14,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=14, width=6,caption="AvgPool"),
            
        to_ConvRelu("conv2", 10, 10,8, offset="(2,0,0)", to="(pool1-east)", height=10, depth=10, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool21", 5, 5,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=5, width=8,caption="AvgPool"),
        
        # 第二帧
        to_Conv("input", 32, 32,3, offset="(0,-10,0)", to="(0,0,0)", height=32, depth=32, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=6, height=6),

        to_ConvRelu("conv12", 28, 28,6, offset="(3,0,0)", to="(input-east)", height=28, depth=28, width=6,caption='conv1'),
        to_connection( "input", "conv12"), 
        to_Pool("pool1", 14, 14,6,offset="(0,0,0)", to="(conv12-east)",height=14, depth=14, width=6,caption="AvgPool"),
            
        to_ConvRelu("conv2", 10, 10,8, offset="(2,0,0)", to="(pool1-east)", height=10, depth=10, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool22", 5, 5,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=5, width=8,caption="AvgPool"),

        # 第七帧
        to_Conv("input", 32, 32,3, offset="(0,-25,0)", to="(0,0,0)", height=32, depth=32, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=6, height=6),
        
        to_ConvRelu("conv17", 28, 28,6, offset="(3,0,0)", to="(input-east)", height=28, depth=28, width=6,caption='conv1'),
        to_connection( "input", "conv17"), 
        to_Pool("pool1", 14, 14,6,offset="(0,0,0)", to="(conv17-east)",height=14, depth=14, width=6,caption="AvgPool"),
        
        to_ConvRelu("conv2", 10, 10,8, offset="(2,0,0)", to="(pool1-east)", height=10, depth=10, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool27", 5, 5,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=5, width=8,caption="AvgPool"),

        # # 省略号
        # to_ellipsis( "conv12", "conv17"),

        # 全连接层
        to_Sum( "sum", offset="(10,10,0)", to="(pool27-east)", radius=2.5, opacity=0.6),
        to_connection( "pool21", "sum"),
        to_connection( "pool22", "sum"),
        to_connection( "pool27", "sum"),

        to_Cascade("cascade", 1, 1400,1, offset="(3,0,0)", to="(sum-east)", height=2.5, depth=280, width=2.5,caption='cascade'),
        to_connection( "sum", "cascade"), 
        

        to_FcRelu_fine("fc1", 1, 64,1, offset="(3,0,0)", to="(cascade-east)", height=2, depth=64, width=2,caption='fc1'),
        to_connection( "cascade", "fc1"), 
        
        to_SoftMax("softMax", 1 ,4,1, offset="(3,0,0)", to="(fc1-east)", height=1, depth=4, width=1, caption="SoftMax"  ),
        to_connection( "fc1", "softMax"), 

        to_end()
        ]
    to_generate(arch, os.getcwd()+'\\draw_houyi\\Net42\\Net42.tex' )
    # end draw_Net42

def draw_Net45():
    arch = [
        to_head( '..' ),
        to_cor(),
        to_begin(),

        # 第一帧
        to_Conv("input", 224, 1,1, offset="(0,0,0)", to="(0,0,0)", height=112, depth=6, width=6,caption='input'),
        
        to_FcRelu("fc1", 1024, 1,1, offset="(3,0,0)", to="(input-east)", height=325, depth=6, width=6,caption='fc1'),
        to_connection( "input", "fc1"), 
            
        to_FcRelu("fc2", 1024, 1,1, offset="(3,0,0)", to="(fc1-east)", height=325, depth=6, width=6,caption='fc2'),
        to_connection( "fc1", "fc2"), 
        
        to_FcRelu("fc3", 256, 1,1, offset="(3,0,0)", to="(fc2-east)", height=128, depth=6, width=6,caption='fc3'),
        to_connection( "fc2", "fc3"), 
    
        to_FcRelu("fc4", 64, 1,1, offset="(3,0,0)", to="(fc3-east)", height=30, depth=6, width=6,caption='fc4'),
        to_connection( "fc3", "fc4"), 

        to_FcRelu_fine("fc5", 16, 1,1, offset="(3,0,0)", to="(fc4-east)", height=16, depth=4, width=4,caption='fc5'),
        to_connection( "fc4", "fc5"), 
        
        to_SoftMax("softMax", 4 ,1,1, offset="(3,0,0)", to="(fc5-east)", height=6, depth=2, width=2, caption="SoftMax"  ),
        to_connection( "fc5", "softMax"), 

        to_end()
        ]
    to_generate(arch, os.getcwd()+'\\draw_houyi\\Net45\\Net45.tex' )
    # end draw_Net45



def draw_Net46():
    arch = [
        to_head( '..' ),
        to_cor(),
        to_begin(),

        # 输入层
        to_Conv("input1", 1, 224,1, offset="(0,0,0)", to="(0,0,0)", height=5, depth=224, width=5,caption='frame1'),
        to_Conv("input2", 1, 224,1, offset="(20,0,0)", to="(input1-east)", height=5, depth=224, width=5,caption='frame2'),
        to_Conv("input3", 1, 224,1, offset="(20,0,0)", to="(input2-east)", height=5, depth=224, width=5,caption='frame3'),
        to_Conv("input4", 1, 224,1, offset="(20,0,0)", to="(input3-east)", height=5, depth=224, width=5,caption='frame4'),
        to_Conv("input5", 1, 224,1, offset="(20,0,0)", to="(input4-east)", height=5, depth=224, width=5,caption='frame5'),
        to_Conv("input6", 1, 224,1, offset="(20,0,0)", to="(input5-east)", height=5, depth=224, width=5,caption='frame6'),
        to_Conv("input7", 1, 224,1, offset="(20,0,0)", to="(input6-east)", height=5, depth=224, width=5,caption='frame7'),
        
        # 第一层
        to_Cascade("node11", 1, 16,1, offset="(0,20,0)", to="(input1-north)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node21", 1, 16,1, offset="(20,0,0)", to="(node11-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node31", 1, 16,1, offset="(20,0,0)", to="(node21-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node41", 1, 16,1, offset="(20,0,0)", to="(node31-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node51", 1, 16,1, offset="(20,0,0)", to="(node41-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node61", 1, 16,1, offset="(20,0,0)", to="(node51-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node71", 1, 16,1, offset="(20,0,0)", to="(node61-east)", height=5, depth=32, width=5,caption=''),
        
        to_connection( "node11", "node21"), 
        to_connection( "node21", "node31"), 
        to_connection( "node31", "node41"), 
        to_connection( "node41", "node51"), 
        to_connection( "node51", "node61"), 
        to_connection( "node61", "node71"), 

        to_connection( "input1", "node11","north","south"), 
        to_connection( "input2", "node21","north","south"), 
        to_connection( "input3", "node31","north","south"), 
        to_connection( "input4", "node41","north","south"), 
        to_connection( "input5", "node51","north","south"), 
        to_connection( "input6", "node61","north","south"), 
        to_connection( "input7", "node71","north","south"), 

        # 第二层
        to_Cascade("node12", 1, 16,1, offset="(0,10,0)", to="(node11-north)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node22", 1, 16,1, offset="(20,0,0)", to="(node12-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node32", 1, 16,1, offset="(20,0,0)", to="(node22-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node42", 1, 16,1, offset="(20,0,0)", to="(node32-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node52", 1, 16,1, offset="(20,0,0)", to="(node42-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node62", 1, 16,1, offset="(20,0,0)", to="(node52-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node72", 1, 16,1, offset="(20,0,0)", to="(node62-east)", height=5, depth=32, width=5,caption=''),

        to_connection( "node12", "node22"), 
        to_connection( "node22", "node32"), 
        to_connection( "node32", "node42"), 
        to_connection( "node42", "node52"), 
        to_connection( "node52", "node62"), 
        to_connection( "node62", "node72"), 

        to_connection( "node11", "node12","north","south"), 
        to_connection( "node21", "node22","north","south"), 
        to_connection( "node31", "node32","north","south"), 
        to_connection( "node41", "node42","north","south"), 
        to_connection( "node51", "node52","north","south"), 
        to_connection( "node61", "node62","north","south"), 
        to_connection( "node71", "node72","north","south"), 

        # 第三层
        to_Cascade("node13", 1, 16,1, offset="(0,10,0)", to="(node12-north)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node23", 1, 16,1, offset="(20,0,0)", to="(node13-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node33", 1, 16,1, offset="(20,0,0)", to="(node23-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node43", 1, 16,1, offset="(20,0,0)", to="(node33-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node53", 1, 16,1, offset="(20,0,0)", to="(node43-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node63", 1, 16,1, offset="(20,0,0)", to="(node53-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node73", 1, 16,1, offset="(20,0,0)", to="(node63-east)", height=5, depth=32, width=5,caption=''),

        to_connection( "node13", "node23"), 
        to_connection( "node23", "node33"), 
        to_connection( "node33", "node43"), 
        to_connection( "node43", "node53"), 
        to_connection( "node53", "node63"), 
        to_connection( "node63", "node73"), 

        to_connection( "node12", "node13","north","south"), 
        to_connection( "node22", "node23","north","south"), 
        to_connection( "node32", "node33","north","south"), 
        to_connection( "node42", "node43","north","south"), 
        to_connection( "node52", "node53","north","south"), 
        to_connection( "node62", "node63","north","south"), 
        to_connection( "node72", "node73","north","south"), 

        # 全连接层
        to_SoftMax("softMax", 1 ,4,1, offset="(0,10,0)", to="(node73-north)", height=4, depth=8, width=4, caption="SoftMax"  ),
        to_connection( "node73", "softMax","north","south"), 

        to_end()
        ]
    to_generate(arch, os.getcwd()+'\\draw_houyi\\Net46\\Net46.tex' )
    # end draw_Net46

def draw_Net47():
    arch = [
        to_head( '..' ),
        to_cor(),
        to_begin(),

        # 输入层
        to_Conv("input1", 1, 224,1, offset="(0,0,0)", to="(0,0,0)", height=5, depth=224, width=5,caption='frame1'),
        to_Conv("input2", 1, 224,1, offset="(20,0,0)", to="(input1-east)", height=5, depth=224, width=5,caption='frame2'),
        to_Conv("input3", 1, 224,1, offset="(20,0,0)", to="(input2-east)", height=5, depth=224, width=5,caption='frame3'),
        to_Conv("input4", 1, 224,1, offset="(20,0,0)", to="(input3-east)", height=5, depth=224, width=5,caption='frame4'),
        to_Conv("input5", 1, 224,1, offset="(20,0,0)", to="(input4-east)", height=5, depth=224, width=5,caption='frame5'),
        to_Conv("input6", 1, 224,1, offset="(20,0,0)", to="(input5-east)", height=5, depth=224, width=5,caption='frame6'),
        to_Conv("input7", 1, 224,1, offset="(20,0,0)", to="(input6-east)", height=5, depth=224, width=5,caption='frame7'),
        
        # 第一层
        to_Cascade("node11", 1, 16,1, offset="(0,20,0)", to="(input1-north)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node21", 1, 16,1, offset="(20,0,0)", to="(node11-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node31", 1, 16,1, offset="(20,0,0)", to="(node21-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node41", 1, 16,1, offset="(20,0,0)", to="(node31-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node51", 1, 16,1, offset="(20,0,0)", to="(node41-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node61", 1, 16,1, offset="(20,0,0)", to="(node51-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node71", 1, 16,1, offset="(20,0,0)", to="(node61-east)", height=5, depth=32, width=5,caption=''),
        
        to_connection( "node11", "node21"), 
        to_connection( "node21", "node31"), 
        to_connection( "node31", "node41"), 
        to_connection( "node41", "node51"), 
        to_connection( "node51", "node61"), 
        to_connection( "node61", "node71"), 

        to_connection( "input1", "node11","north","south"), 
        to_connection( "input2", "node21","north","south"), 
        to_connection( "input3", "node31","north","south"), 
        to_connection( "input4", "node41","north","south"), 
        to_connection( "input5", "node51","north","south"), 
        to_connection( "input6", "node61","north","south"), 
        to_connection( "input7", "node71","north","south"), 

        # 第二层
        to_Cascade("node12", 1, 16,1, offset="(0,10,0)", to="(node11-north)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node22", 1, 16,1, offset="(20,0,0)", to="(node12-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node32", 1, 16,1, offset="(20,0,0)", to="(node22-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node42", 1, 16,1, offset="(20,0,0)", to="(node32-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node52", 1, 16,1, offset="(20,0,0)", to="(node42-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node62", 1, 16,1, offset="(20,0,0)", to="(node52-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node72", 1, 16,1, offset="(20,0,0)", to="(node62-east)", height=5, depth=32, width=5,caption=''),

        to_connection( "node12", "node22"), 
        to_connection( "node22", "node32"), 
        to_connection( "node32", "node42"), 
        to_connection( "node42", "node52"), 
        to_connection( "node52", "node62"), 
        to_connection( "node62", "node72"), 

        to_connection( "node11", "node12","north","south"), 
        to_connection( "node21", "node22","north","south"), 
        to_connection( "node31", "node32","north","south"), 
        to_connection( "node41", "node42","north","south"), 
        to_connection( "node51", "node52","north","south"), 
        to_connection( "node61", "node62","north","south"), 
        to_connection( "node71", "node72","north","south"), 

        # 第三层
        to_Cascade("node13", 1, 16,1, offset="(0,10,0)", to="(node12-north)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node23", 1, 16,1, offset="(20,0,0)", to="(node13-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node33", 1, 16,1, offset="(20,0,0)", to="(node23-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node43", 1, 16,1, offset="(20,0,0)", to="(node33-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node53", 1, 16,1, offset="(20,0,0)", to="(node43-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node63", 1, 16,1, offset="(20,0,0)", to="(node53-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node73", 1, 16,1, offset="(20,0,0)", to="(node63-east)", height=5, depth=32, width=5,caption=''),

        to_connection( "node13", "node23"), 
        to_connection( "node23", "node33"), 
        to_connection( "node33", "node43"), 
        to_connection( "node43", "node53"), 
        to_connection( "node53", "node63"), 
        to_connection( "node63", "node73"), 

        to_connection( "node12", "node13","north","south"), 
        to_connection( "node22", "node23","north","south"), 
        to_connection( "node32", "node33","north","south"), 
        to_connection( "node42", "node43","north","south"), 
        to_connection( "node52", "node53","north","south"), 
        to_connection( "node62", "node63","north","south"), 
        to_connection( "node72", "node73","north","south"), 

        # 全连接层
        to_Sum( "sum", offset="(0,20,0)", to="(node43-north)", radius=2.5, opacity=0.6),
        to_connection( "node13", "sum","north","south"), 
        to_connection( "node23", "sum","north","south"), 
        to_connection( "node33", "sum","north","south"), 
        to_connection( "node43", "sum","north","south"), 
        to_connection( "node53", "sum","north","south"), 
        to_connection( "node63", "sum","north","south"), 
        to_connection( "node73", "sum","north","south"), 


        to_Cascade("cascade", 1,112,1, offset="(0,10,0)", to="(sum-north)", height=5, depth=112, width=5,caption='cascade'),
        to_connection( "sum", "cascade","north","south"), 

        to_SoftMax("softMax", 1 ,4,1, offset="(0,10,0)", to="(cascade-north)", height=4, depth=8, width=4, caption="SoftMax"  ),
        to_connection( "cascade", "softMax","north","south"), 

        to_end()
        ]
    to_generate(arch, os.getcwd()+'\\draw_houyi\\Net47\\Net47.tex' )
    # end draw_Net47



def draw_Net48():
    arch = [
        to_head( '..' ),
        to_cor(),
        to_begin(),

        # 第一帧
        # CNN 模块
        to_Conv("input", 32, 32,3, offset="(0,0,0)", to="(0,0,0)", height=32, depth=32, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=6, height=6),
        
        to_ConvRelu("conv1", 28, 28,6, offset="(3,0,0)", to="(input-east)", height=28, depth=28, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 14,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=14, width=6,caption="AvgPool"),
            
        to_ConvRelu("conv2", 10, 10,8, offset="(2,0,0)", to="(pool1-east)", height=10, depth=10, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool21", 5, 5,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=5, width=8,caption="AvgPool"),
        # LSTM 模块
        to_Conv("input1", 1, 200,1, offset="(5,0,0)", to="(pool21-east)", height=2.5, depth=100, width=2.5,caption='frame1'),
        to_Cascade("node11", 1, 16,1, offset="(6,0,0)", to="(input1-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node21", 1, 16,1, offset="(3,0,0)", to="(node11-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node31", 1, 16,1, offset="(3,0,0)", to="(node21-east)", height=2.5, depth=8, width=2.5,caption=''),
        
        to_connection( "pool21", "input1"), 
        to_connection( "input1", "node11"), 
        to_connection( "node11", "node21"), 
        to_connection( "node21", "node31"), 


        # 第二帧
        # CNN 模块
        to_Conv("input", 32, 32,3, offset="(0,-10,0)", to="(0,0,0)", height=32, depth=32, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=6, height=6),

        to_ConvRelu("conv12", 28, 28,6, offset="(3,0,0)", to="(input-east)", height=28, depth=28, width=6,caption='conv1'),
        to_connection( "input", "conv12"), 
        to_Pool("pool1", 14, 14,6,offset="(0,0,0)", to="(conv12-east)",height=14, depth=14, width=6,caption="AvgPool"),
            
        to_ConvRelu("conv2", 10, 10,8, offset="(2,0,0)", to="(pool1-east)", height=10, depth=10, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool22", 5, 5,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=5, width=8,caption="AvgPool"),
        # LSTM 模块
        to_Conv("input2", 1, 200,1, offset="(5,0,0)", to="(pool22-east)", height=2.5, depth=100, width=2.5,caption='frame1'),
        to_Cascade("node12", 1, 16,1, offset="(6,0,0)", to="(input2-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node22", 1, 16,1, offset="(3,0,0)", to="(node12-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node32", 1, 16,1, offset="(3,0,0)", to="(node22-east)", height=2.5, depth=8, width=2.5,caption=''),
        
        to_connection( "pool22", "input2"), 
        to_connection( "input2", "node12"), 
        to_connection( "node12", "node22"), 
        to_connection( "node22", "node32"), 
        
        to_transNode("transNode11",offset="(0,-4,0)", to="(node12-south)"),
        to_transNode("transNode21",offset="(0,-4,0)", to="(node22-south)"),
        to_transNode("transNode31",offset="(0,-4,0)", to="(node32-south)"),

        to_connection( "node11", "node12","south","north"), 
        to_connection( "node21", "node22","south","north"), 
        to_connection( "node31", "node32","south","north"), 

        to_connection( "node12", "transNode11","south","north"), 
        to_connection( "node22", "transNode21","south","north"), 
        to_connection( "node32", "transNode31","south","north"), 


        # 第七帧
        # CNN 模块
        to_Conv("input", 32, 32,3, offset="(0,-25,0)", to="(0,0,0)", height=32, depth=32, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=6, height=6),
        
        to_ConvRelu("conv17", 28, 28,6, offset="(3,0,0)", to="(input-east)", height=28, depth=28, width=6,caption='conv1'),
        to_connection( "input", "conv17"), 
        to_Pool("pool1", 14, 14,6,offset="(0,0,0)", to="(conv17-east)",height=14, depth=14, width=6,caption="AvgPool"),
        
        to_ConvRelu("conv2", 10, 10,8, offset="(2,0,0)", to="(pool1-east)", height=10, depth=10, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool27", 5, 5,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=5, width=8,caption="AvgPool"),
        # LSTM 模块
        to_Conv("input7", 1, 200,1, offset="(5,0,0)", to="(pool27-east)", height=2.5, depth=100, width=2.5,caption='frame1'),
        to_Cascade("node17", 1, 16,1, offset="(6,0,0)", to="(input7-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node27", 1, 16,1, offset="(3,0,0)", to="(node17-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node37", 1, 16,1, offset="(3,0,0)", to="(node27-east)", height=2.5, depth=8, width=2.5,caption=''),
        
        to_connection( "pool27", "input7"), 
        to_connection( "input7", "node17"), 
        to_connection( "node17", "node27"), 
        to_connection( "node27", "node37"),        
       
        to_transNode("transNode12", offset="(0,4,0)", to="(node17-south)"),
        to_transNode("transNode22", offset="(0,4,0)", to="(node27-south)"),
        to_transNode("transNode32", offset="(0,4,0)", to="(node37-south)"),
        
        to_connection( "transNode12", "node17","south","north"), 
        to_connection( "transNode22", "node27","south","north"), 
        to_connection( "transNode32", "node37","south","north"), 

        # # 省略号
        # to_ellipsis( "conv12", "conv17"),

        # 全连接层
        to_SoftMax("softMax", 1 ,4,1, offset="(3,0,0)", to="(node37-east)", height=2, depth=5, width=2, caption="SoftMax"  ),
        to_connection( "node37", "softMax"), 

        to_end()
        ]
    to_generate(arch, os.getcwd()+'\\draw_houyi\\Net48\\Net48.tex' )
    # end draw_Net48


def draw_Net49():
    arch = [
        to_head( '..' ),
        to_cor(),
        to_begin(),

        # 第一帧
        # CNN 模块        
        to_Conv("input", 32, 96,3, offset="(0,0,0)", to="(0,0,0)", height=32, depth=96, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=18, height=6),
        
        to_ConvRelu("conv1", 28, 82,6, offset="(3,0,0)", to="(input-east)", height=28, depth=82, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 40,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=40, width=6,caption="MaxPool"),
            
        to_ConvRelu("conv2", 10, 26,8, offset="(3,0,0)", to="(pool1-east)", height=10, depth=26, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool2", 5, 12,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=12, width=8,caption="MaxPool"),
        
        to_ConvRelu("conv3", 5, 12,8, offset="(2,0,0)", to="(pool2-east)", height=5, depth=12, width=8,caption='conv3'),
        to_connection( "pool2", "conv3"), 
        to_Pool("pool31", 2, 4,8,offset="(0,0,0)", to="(conv3-east)",height=2, depth=4, width=8,caption="MaxPool"),
        # LSTM 模块
        to_Conv("input1", 1, 64,1, offset="(5,0,0)", to="(pool31-east)", height=2.5, depth=64, width=2.5,caption='frame1'),
        to_Cascade("node11", 1, 8,1, offset="(6,0,0)", to="(input1-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node21", 1, 8,1, offset="(3,0,0)", to="(node11-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node31", 1, 8,1, offset="(3,0,0)", to="(node21-east)", height=2.5, depth=8, width=2.5,caption=''),
        
        to_connection( "pool31", "input1"), 
        to_connection( "input1", "node11"), 
        to_connection( "node11", "node21"), 
        to_connection( "node21", "node31"), 

        # 第二帧
        to_Conv("input", 32, 96,3, offset="(0,15,0)", to="(0,0,0)", height=32, depth=96, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=18, height=6),
        
        to_ConvRelu("conv1", 28, 82,6, offset="(3,0,0)", to="(input-east)", height=28, depth=82, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 40,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=40, width=6,caption="MaxPool"),
            
        to_ConvRelu("conv2", 10, 26,8, offset="(3,0,0)", to="(pool1-east)", height=10, depth=26, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool2", 5, 12,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=12, width=8,caption="MaxPool"),
        
        to_ConvRelu("conv3", 5, 12,8, offset="(2,0,0)", to="(pool2-east)", height=5, depth=12, width=8,caption='conv3'),
        to_connection( "pool2", "conv3"), 
        to_Pool("pool32", 2, 4,8,offset="(0,0,0)", to="(conv3-east)",height=2, depth=4, width=8,caption="MaxPool"),
        # LSTM 模块
        to_Conv("input2", 1, 64,1, offset="(5,0,0)", to="(pool32-east)", height=2.5, depth=64, width=2.5,caption='frame2'),
        to_Cascade("node12", 1, 8,1, offset="(6,0,0)", to="(input2-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node22", 1, 8,1, offset="(3,0,0)", to="(node12-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node32", 1, 8,1, offset="(3,0,0)", to="(node22-east)", height=2.5, depth=8, width=2.5,caption=''),
        
        to_connection( "pool32", "input2"), 
        to_connection( "input2", "node12"), 
        to_connection( "node12", "node22"), 
        to_connection( "node22", "node32"), 

        # 第三帧
        to_Conv("input", 32, 96,3, offset="(0,30,0)", to="(0,0,0)", height=32, depth=96, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=18, height=6),
        
        to_ConvRelu("conv1", 28, 82,6, offset="(3,0,0)", to="(input-east)", height=28, depth=82, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 40,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=40, width=6,caption="MaxPool"),
            
        to_ConvRelu("conv2", 10, 26,8, offset="(3,0,0)", to="(pool1-east)", height=10, depth=26, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool2", 5, 12,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=12, width=8,caption="MaxPool"),
        
        to_ConvRelu("conv3", 5, 12,8, offset="(2,0,0)", to="(pool2-east)", height=5, depth=12, width=8,caption='conv3'),
        to_connection( "pool2", "conv3"), 
        to_Pool("pool33", 2, 4,8,offset="(0,0,0)", to="(conv3-east)",height=2, depth=4, width=8,caption="MaxPool"),
        # LSTM 模块
        to_Conv("input3", 1, 64,1, offset="(5,0,0)", to="(pool33-east)", height=2.5, depth=64, width=2.5,caption='frame3'),
        to_Cascade("node13", 1, 8,1, offset="(6,0,0)", to="(input3-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node23", 1, 8,1, offset="(3,0,0)", to="(node13-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node33", 1, 8,1, offset="(3,0,0)", to="(node23-east)", height=2.5, depth=8, width=2.5,caption=''),
        
        to_connection( "pool33", "input3"), 
        to_connection( "input3", "node13"), 
        to_connection( "node13", "node23"), 
        to_connection( "node23", "node33"), 

        # 第四帧
        to_Conv("input", 32, 96,3, offset="(0,45,0)", to="(0,0,0)", height=32, depth=96, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=18, height=6),
        
        to_ConvRelu("conv1", 28, 82,6, offset="(3,0,0)", to="(input-east)", height=28, depth=82, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 40,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=40, width=6,caption="MaxPool"),
            
        to_ConvRelu("conv2", 10, 26,8, offset="(3,0,0)", to="(pool1-east)", height=10, depth=26, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool2", 5, 12,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=12, width=8,caption="MaxPool"),
        
        to_ConvRelu("conv3", 5, 12,8, offset="(2,0,0)", to="(pool2-east)", height=5, depth=12, width=8,caption='conv3'),
        to_connection( "pool2", "conv3"), 
        to_Pool("pool34", 2, 4,8,offset="(0,0,0)", to="(conv3-east)",height=2, depth=4, width=8,caption="MaxPool"),
        # LSTM 模块
        to_Conv("input4", 1, 64,1, offset="(5,0,0)", to="(pool34-east)", height=2.5, depth=64, width=2.5,caption='frame4'),
        to_Cascade("node14", 1, 8,1, offset="(6,0,0)", to="(input4-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node24", 1, 8,1, offset="(3,0,0)", to="(node14-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node34", 1, 8,1, offset="(3,0,0)", to="(node24-east)", height=2.5, depth=8, width=2.5,caption=''),
        
        to_connection( "pool34", "input4"), 
        to_connection( "input4", "node14"), 
        to_connection( "node14", "node24"), 
        to_connection( "node24", "node34"), 
        
        # 全连接层
        to_Sum( "sum", offset="(12,7,0)", to="(node32-east)", radius=2.5, opacity=0.6),
        to_connection( "node31", "sum"),
        to_connection( "node32", "sum"),
        to_connection( "node33", "sum"),
        to_connection( "node34", "sum"),

        to_Cascade("cascade", 1, 32,1, offset="(5,0,0)", to="(sum-east)", height=2.5, depth=32, width=2.5,caption='cascade'),
        to_connection( "sum", "cascade"), 
        
        to_SoftMax("softMax", 1 ,4,1, offset="(3,0,0)", to="(cascade-east)", height=2, depth=5, width=2, caption="SoftMax"  ),
        to_connection( "cascade", "softMax"), 

        to_end()
        ]
    to_generate(arch, os.getcwd()+'\\draw_houyi\\Net49\\Net49.tex' )
    # end draw_Net49



def draw_Net2():
    arch = [
        to_head( '..' ),
        to_cor(),
        to_begin(),

        # 第一帧
        to_Conv("input", 32, 96,3, offset="(0,0,0)", to="(0,0,0)", height=32, depth=96, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=18, height=6),
        
        to_ConvRelu("conv1", 28, 82,6, offset="(3,0,0)", to="(input-east)", height=28, depth=82, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 40,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=40, width=6,caption="MaxPool"),
            
        to_ConvRelu("conv2", 10, 26,8, offset="(3,0,0)", to="(pool1-east)", height=10, depth=26, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool2", 5, 12,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=12, width=8,caption="MaxPool"),
        
        to_ConvRelu("conv3", 5, 12,8, offset="(2,0,0)", to="(pool2-east)", height=5, depth=12, width=8,caption='conv3'),
        to_connection( "pool2", "conv3"), 
        to_Pool("pool31", 2, 4,8,offset="(0,0,0)", to="(conv3-east)",height=2, depth=4, width=8,caption="MaxPool"),
        
        # 第二帧
        to_Conv("input", 32, 96,3, offset="(0,15,0)", to="(0,0,0)", height=32, depth=96, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=18, height=6),
        
        to_ConvRelu("conv1", 28, 82,6, offset="(3,0,0)", to="(input-east)", height=28, depth=82, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 40,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=40, width=6,caption="MaxPool"),
            
        to_ConvRelu("conv2", 10, 26,8, offset="(3,0,0)", to="(pool1-east)", height=10, depth=26, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool2", 5, 12,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=12, width=8,caption="MaxPool"),
        
        to_ConvRelu("conv3", 5, 12,8, offset="(2,0,0)", to="(pool2-east)", height=5, depth=12, width=8,caption='conv3'),
        to_connection( "pool2", "conv3"), 
        to_Pool("pool32", 2, 4,8,offset="(0,0,0)", to="(conv3-east)",height=2, depth=4, width=8,caption="MaxPool"),

        # 第三帧
        to_Conv("input", 32, 96,3, offset="(0,30,0)", to="(0,0,0)", height=32, depth=96, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=18, height=6),
        
        to_ConvRelu("conv1", 28, 82,6, offset="(3,0,0)", to="(input-east)", height=28, depth=82, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 40,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=40, width=6,caption="MaxPool"),
            
        to_ConvRelu("conv2", 10, 26,8, offset="(3,0,0)", to="(pool1-east)", height=10, depth=26, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool2", 5, 12,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=12, width=8,caption="MaxPool"),
        
        to_ConvRelu("conv3", 5, 12,8, offset="(2,0,0)", to="(pool2-east)", height=5, depth=12, width=8,caption='conv3'),
        to_connection( "pool2", "conv3"), 
        to_Pool("pool33", 2, 4,8,offset="(0,0,0)", to="(conv3-east)",height=2, depth=4, width=8,caption="MaxPool"),

        # 第四帧
        to_Conv("input", 32, 96,3, offset="(0,45,0)", to="(0,0,0)", height=32, depth=96, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=18, height=6),
        
        to_ConvRelu("conv1", 28, 82,6, offset="(3,0,0)", to="(input-east)", height=28, depth=82, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 40,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=40, width=6,caption="MaxPool"),
            
        to_ConvRelu("conv2", 10, 26,8, offset="(3,0,0)", to="(pool1-east)", height=10, depth=26, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool2", 5, 12,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=12, width=8,caption="MaxPool"),
        
        to_ConvRelu("conv3", 5, 12,8, offset="(2,0,0)", to="(pool2-east)", height=5, depth=12, width=8,caption='conv3'),
        to_connection( "pool2", "conv3"), 
        to_Pool("pool34", 2, 4,8,offset="(0,0,0)", to="(conv3-east)",height=2, depth=4, width=8,caption="MaxPool"),

        # 全连接层
        to_Sum( "sum", offset="(12,7,0)", to="(pool32-east)", radius=2.5, opacity=0.6),
        to_connection( "pool31", "sum"),
        to_connection( "pool32", "sum"),
        to_connection( "pool33", "sum"),
        to_connection( "pool34", "sum"),

        to_Cascade("cascade", 1, 256,1, offset="(5,0,0)", to="(sum-east)", height=3.5, depth=256, width=3.5,caption='cascade'),
        to_connection( "sum", "cascade"), 

        to_FcRelu_fine("fc1", 1, 32,1, offset="(3,0,0)", to="(cascade-east)", height=2.5, depth=32, width=2.5,caption='fc1'),
        to_connection( "cascade", "fc1"), 

        to_FcRelu_fine("fc2", 1, 8,1, offset="(3,0,0)", to="(fc1-east)", height=2.5, depth=8, width=2.5,caption='fc2'),
        to_connection( "fc1", "fc2"), 
        
        to_SoftMax("softMax", 1 ,2,1, offset="(3,0,0)", to="(fc2-east)", height=1, depth=2, width=1, caption="SoftMax"  ),
        to_connection( "fc2", "softMax"), 

        to_end()
        ]
    to_generate(arch, os.getcwd()+'\\draw_houyi\\Net2\\Net2.tex' )
    # end draw_Net2


def draw_Net22():
    arch = [
        to_head( '..' ),
        to_cor(),
        to_begin(),

        # 第一帧
        to_Conv("input", 32, 32,3, offset="(0,0,0)", to="(0,0,0)", height=32, depth=32, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=6, height=6),
        
        to_ConvRelu("conv1", 28, 28,6, offset="(3,0,0)", to="(input-east)", height=28, depth=28, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 14,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=14, width=6,caption="AvgPool"),
            
        to_ConvRelu("conv2", 10, 10,8, offset="(2,0,0)", to="(pool1-east)", height=10, depth=10, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool21", 5, 5,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=5, width=8,caption="AvgPool"),
        
        # 第二帧
        to_Conv("input", 32, 32,3, offset="(0,-10,0)", to="(0,0,0)", height=32, depth=32, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=6, height=6),

        to_ConvRelu("conv12", 28, 28,6, offset="(3,0,0)", to="(input-east)", height=28, depth=28, width=6,caption='conv1'),
        to_connection( "input", "conv12"), 
        to_Pool("pool1", 14, 14,6,offset="(0,0,0)", to="(conv12-east)",height=14, depth=14, width=6,caption="AvgPool"),
            
        to_ConvRelu("conv2", 10, 10,8, offset="(2,0,0)", to="(pool1-east)", height=10, depth=10, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool22", 5, 5,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=5, width=8,caption="AvgPool"),

        # 第七帧
        to_Conv("input", 32, 32,3, offset="(0,-25,0)", to="(0,0,0)", height=32, depth=32, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=6, height=6),
        
        to_ConvRelu("conv17", 28, 28,6, offset="(3,0,0)", to="(input-east)", height=28, depth=28, width=6,caption='conv1'),
        to_connection( "input", "conv17"), 
        to_Pool("pool1", 14, 14,6,offset="(0,0,0)", to="(conv17-east)",height=14, depth=14, width=6,caption="AvgPool"),
        
        to_ConvRelu("conv2", 10, 10,8, offset="(2,0,0)", to="(pool1-east)", height=10, depth=10, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool27", 5, 5,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=5, width=8,caption="AvgPool"),

        # # 省略号
        # to_ellipsis( "conv12", "conv17"),

        # 全连接层
        to_Sum( "sum", offset="(10,10,0)", to="(pool27-east)", radius=2.5, opacity=0.6),
        to_connection( "pool21", "sum"),
        to_connection( "pool22", "sum"),
        to_connection( "pool27", "sum"),

        to_Cascade("cascade", 1, 1400,1, offset="(3,0,0)", to="(sum-east)", height=2.5, depth=280, width=2.5,caption='cascade'),
        to_connection( "sum", "cascade"), 
        

        to_FcRelu_fine("fc1", 1, 64,1, offset="(3,0,0)", to="(cascade-east)", height=2, depth=64, width=2,caption='fc1'),
        to_connection( "cascade", "fc1"), 
        
        to_FcRelu_fine("fc2", 1, 16,1, offset="(3,0,0)", to="(fc1-east)", height=2, depth=16, width=2,caption='fc2'),
        to_connection( "fc1", "fc2"), 

        to_SoftMax("softMax", 1 ,2,1, offset="(3,0,0)", to="(fc2-east)", height=1, depth=2, width=1, caption="SoftMax"  ),
        to_connection( "fc2", "softMax"), 

        to_end()
        ]
    to_generate(arch, os.getcwd()+'\\draw_houyi\\Net22\\Net22.tex' )
    # end draw_Net22


def draw_Net23():
    arch = [
        to_head( '..' ),
        to_cor(),
        to_begin(),

        # 输入层
        to_Conv("input1", 1, 32,1, offset="(0,0,0)", to="(0,0,0)", height=4, depth=32, width=4,caption='frame1'),
        to_Conv("input4", 1, 32,1, offset="(30,0,0)", to="(input1-east)", height=4, depth=32, width=4,caption='frame4'),
        to_Conv("input7", 1, 32,1, offset="(30,0,0)", to="(input4-east)", height=4, depth=32, width=4,caption='frame7'),
        
        # 第一层
        to_Cascade("node11", 1, 16,1, offset="(0,12,0)", to="(input1-north)", height=4, depth=16, width=4,caption=''),
        to_transNode("transNode21",offset="(8,0,0)", to="(node11-east)"),
        to_transNode("transNode31",offset="(14,0,0)", to="(transNode21-east)"),
        to_Cascade("node41", 1, 16,1, offset="(30,0,0)", to="(node11-east)", height=4, depth=16, width=4,caption=''),
        to_transNode("transNode51",offset="(8,0,0)", to="(node41-east)"),
        to_transNode("transNode61",offset="(14,0,0)", to="(transNode51-east)"),
        to_Cascade("node71", 1, 16,1, offset="(30,0,0)", to="(node41-east)", height=4, depth=16, width=4,caption=''),
        
        to_connection( "node11", "transNode21"), 
        to_connection( "transNode31", "node41"), 
        to_connection( "node41", "transNode51"), 
        to_connection( "transNode61", "node71"), 

        to_connection( "input1", "node11","north","south"), 
        to_connection( "input4", "node41","north","south"), 
        to_connection( "input7", "node71","north","south"), 

        # 第二层
        to_Cascade("node12", 1, 16,1, offset="(0,10,0)", to="(node11-north)", height=4, depth=16, width=4,caption=''),
        to_transNode("transNode22",offset="(8,0,0)", to="(node12-east)"),
        to_transNode("transNode32",offset="(14,0,0)", to="(transNode22-east)"),        
        to_Cascade("node42", 1, 16,1, offset="(30,0,0)", to="(node12-east)", height=4, depth=16, width=4,caption=''),
        to_transNode("transNode52",offset="(8,0,0)", to="(node42-east)"),
        to_transNode("transNode62",offset="(14,0,0)", to="(transNode52-east)"),
        to_Cascade("node72", 1, 16,1, offset="(30,0,0)", to="(node42-east)", height=4, depth=16, width=4,caption=''),

        to_connection( "node12", "transNode22"), 
        to_connection( "transNode32", "node42"), 
        to_connection( "node42", "transNode52"), 
        to_connection( "transNode62", "node72"), 

        to_connection( "node11", "node12","north","south"), 
        to_connection( "node41", "node42","north","south"), 
        to_connection( "node71", "node72","north","south"), 

        # 第三层
        to_Cascade("node13", 1, 16,1, offset="(0,10,0)", to="(node12-north)", height=4, depth=16, width=4,caption=''),
        to_transNode("transNode23",offset="(8,0,0)", to="(node13-east)"),
        to_transNode("transNode33",offset="(14,0,0)", to="(transNode23-east)"), 
        to_Cascade("node43", 1, 16,1, offset="(30,0,0)", to="(node13-east)", height=4, depth=16, width=4,caption=''),
        to_transNode("transNode53",offset="(8,0,0)", to="(node43-east)"),
        to_transNode("transNode63",offset="(14,0,0)", to="(transNode53-east)"),
        to_Cascade("node73", 1, 16,1, offset="(30,0,0)", to="(node43-east)", height=4, depth=16, width=4,caption=''),

        to_connection( "node13", "transNode23"),  
        to_connection( "transNode33", "node43"), 
        to_connection( "node43", "transNode53"), 
        to_connection( "transNode63", "node73"), 

        to_connection( "node12", "node13","north","south"), 
        to_connection( "node42", "node43","north","south"), 
        to_connection( "node72", "node73","north","south"), 

        # 全连接层
        to_SoftMax("softMax", 1 ,2,1, offset="(0,10,0)", to="(node73-north)", height=3, depth=6, width=3, caption="SoftMax"  ),
        to_connection( "node73", "softMax","north","south"), 

        to_end()
        ]
    to_generate(arch, os.getcwd()+'\\draw_houyi\\Net23\\Net23.tex' )
    # end draw_Net23



def draw_Net24():
    arch = [
        to_head( '..' ),
        to_cor(),
        to_begin(),

        # 输入层
        to_Conv("input1", 1, 32,1, offset="(0,0,0)", to="(0,0,0)", height=4, depth=32, width=4,caption='frame1'),
        to_Conv("input4", 1, 32,1, offset="(30,0,0)", to="(input1-east)", height=4, depth=32, width=4,caption='frame4'),
        to_Conv("input7", 1, 32,1, offset="(30,0,0)", to="(input4-east)", height=4, depth=32, width=4,caption='frame7'),
        
        # 第一层
        to_Cascade("node11", 1, 16,1, offset="(0,12,0)", to="(input1-north)", height=4, depth=16, width=4,caption=''),
        to_transNode("transNode21",offset="(8,0,0)", to="(node11-east)"),
        to_transNode("transNode31",offset="(14,0,0)", to="(transNode21-east)"),
        to_Cascade("node41", 1, 16,1, offset="(30,0,0)", to="(node11-east)", height=4, depth=16, width=4,caption=''),
        to_transNode("transNode51",offset="(8,0,0)", to="(node41-east)"),
        to_transNode("transNode61",offset="(14,0,0)", to="(transNode51-east)"),
        to_Cascade("node71", 1, 16,1, offset="(30,0,0)", to="(node41-east)", height=4, depth=16, width=4,caption=''),
        
        to_connection( "node11", "transNode21"), 
        to_connection( "transNode31", "node41"), 
        to_connection( "node41", "transNode51"), 
        to_connection( "transNode61", "node71"), 

        to_connection( "input1", "node11","north","south"), 
        to_connection( "input4", "node41","north","south"), 
        to_connection( "input7", "node71","north","south"), 

        # 第二层
        to_Cascade("node12", 1, 16,1, offset="(0,10,0)", to="(node11-north)", height=4, depth=16, width=4,caption=''),
        to_transNode("transNode22",offset="(8,0,0)", to="(node12-east)"),
        to_transNode("transNode32",offset="(14,0,0)", to="(transNode22-east)"),        
        to_Cascade("node42", 1, 16,1, offset="(30,0,0)", to="(node12-east)", height=4, depth=16, width=4,caption=''),
        to_transNode("transNode52",offset="(8,0,0)", to="(node42-east)"),
        to_transNode("transNode62",offset="(14,0,0)", to="(transNode52-east)"),
        to_Cascade("node72", 1, 16,1, offset="(30,0,0)", to="(node42-east)", height=4, depth=16, width=4,caption=''),

        to_connection( "node12", "transNode22"), 
        to_connection( "transNode32", "node42"), 
        to_connection( "node42", "transNode52"), 
        to_connection( "transNode62", "node72"), 

        to_connection( "node11", "node12","north","south"), 
        to_connection( "node41", "node42","north","south"), 
        to_connection( "node71", "node72","north","south"), 

        # 第三层
        to_Cascade("node13", 1, 16,1, offset="(0,10,0)", to="(node12-north)", height=4, depth=16, width=4,caption=''),
        to_transNode("transNode23",offset="(8,0,0)", to="(node13-east)"),
        to_transNode("transNode33",offset="(14,0,0)", to="(transNode23-east)"), 
        to_Cascade("node43", 1, 16,1, offset="(30,0,0)", to="(node13-east)", height=4, depth=16, width=4,caption=''),
        to_transNode("transNode53",offset="(8,0,0)", to="(node43-east)"),
        to_transNode("transNode63",offset="(14,0,0)", to="(transNode53-east)"),
        to_Cascade("node73", 1, 16,1, offset="(30,0,0)", to="(node43-east)", height=4, depth=16, width=4,caption=''),

        to_connection( "node13", "transNode23"),  
        to_connection( "transNode33", "node43"), 
        to_connection( "node43", "transNode53"), 
        to_connection( "transNode63", "node73"), 

        to_connection( "node12", "node13","north","south"), 
        to_connection( "node42", "node43","north","south"), 
        to_connection( "node72", "node73","north","south"), 

        # 全连接层
        to_Sum( "sum", offset="(0,10,0)", to="(node43-north)", radius=2.5, opacity=0.6),
        to_connection( "node13", "sum","north","south"), 
        to_connection( "node43", "sum","north","south"), 
        to_connection( "node73", "sum","north","south"), 


        to_Cascade("cascade", 1,4096,1, offset="(0,10,0)", to="(sum-north)", height=5, depth=112, width=5,caption='cascade'),
        to_connection( "sum", "cascade","north","south"), 

        to_FcRelu_fine("fc1", 1, 128,1, offset="(0,8,0)", to="(cascade-north)", height=5, depth=32, width=5,caption='fc1'),
        to_connection( "cascade", "fc1","north","south"), 

        to_FcRelu_fine("fc2", 1, 16,1, offset="(0,8,0)", to="(fc1-north)", height=5, depth=16, width=5,caption='fc1'),
        to_connection( "fc1", "fc2","north","south"), 

        to_SoftMax("softMax", 1 ,2,1, offset="(0,5,0)", to="(fc2-north)", height=3, depth=6, width=3, caption="SoftMax"  ),
        to_connection( "fc2", "softMax","north","south"), 

        to_end()
        ]
    to_generate(arch, os.getcwd()+'\\draw_houyi\\Net24\\Net24.tex' )
    # end draw_Net24


def draw_Net25():
    arch = [
        to_head( '..' ),
        to_cor(),
        to_begin(),

        # 第一帧
        to_Conv("input", 224, 1,1, offset="(0,0,0)", to="(0,0,0)", height=112, depth=6, width=6,caption='input'),
        
        to_FcRelu("fc1", 1024, 1,1, offset="(3,0,0)", to="(input-east)", height=325, depth=6, width=6,caption='fc1'),
        to_connection( "input", "fc1"), 
            
        to_FcRelu("fc2", 1024, 1,1, offset="(3,0,0)", to="(fc1-east)", height=325, depth=6, width=6,caption='fc2'),
        to_connection( "fc1", "fc2"), 
        
        to_FcRelu("fc3", 256, 1,1, offset="(3,0,0)", to="(fc2-east)", height=128, depth=6, width=6,caption='fc3'),
        to_connection( "fc2", "fc3"), 
    
        to_FcRelu("fc4", 64, 1,1, offset="(3,0,0)", to="(fc3-east)", height=30, depth=6, width=6,caption='fc4'),
        to_connection( "fc3", "fc4"), 

        to_FcRelu_fine("fc5", 16, 1,1, offset="(3,0,0)", to="(fc4-east)", height=16, depth=4, width=4,caption='fc5'),
        to_connection( "fc4", "fc5"), 
        
        to_SoftMax("softMax", 2 ,1,1, offset="(3,0,0)", to="(fc5-east)", height=3, depth=2, width=2, caption="SoftMax"  ),
        to_connection( "fc5", "softMax"), 

        to_end()
        ]
    to_generate(arch, os.getcwd()+'\\draw_houyi\\Net25\\Net25.tex' )
    # end draw_Net25



def draw_Net26():
    arch = [
        to_head( '..' ),
        to_cor(),
        to_begin(),

        # 输入层
        to_Conv("input1", 1, 224,1, offset="(0,0,0)", to="(0,0,0)", height=5, depth=224, width=5,caption='frame1'),
        to_Conv("input2", 1, 224,1, offset="(20,0,0)", to="(input1-east)", height=5, depth=224, width=5,caption='frame2'),
        to_Conv("input3", 1, 224,1, offset="(20,0,0)", to="(input2-east)", height=5, depth=224, width=5,caption='frame3'),
        to_Conv("input4", 1, 224,1, offset="(20,0,0)", to="(input3-east)", height=5, depth=224, width=5,caption='frame4'),
        to_Conv("input5", 1, 224,1, offset="(20,0,0)", to="(input4-east)", height=5, depth=224, width=5,caption='frame5'),
        to_Conv("input6", 1, 224,1, offset="(20,0,0)", to="(input5-east)", height=5, depth=224, width=5,caption='frame6'),
        to_Conv("input7", 1, 224,1, offset="(20,0,0)", to="(input6-east)", height=5, depth=224, width=5,caption='frame7'),
        
        # 第一层
        to_Cascade("node11", 1, 16,1, offset="(0,20,0)", to="(input1-north)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node21", 1, 16,1, offset="(20,0,0)", to="(node11-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node31", 1, 16,1, offset="(20,0,0)", to="(node21-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node41", 1, 16,1, offset="(20,0,0)", to="(node31-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node51", 1, 16,1, offset="(20,0,0)", to="(node41-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node61", 1, 16,1, offset="(20,0,0)", to="(node51-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node71", 1, 16,1, offset="(20,0,0)", to="(node61-east)", height=5, depth=32, width=5,caption=''),
        
        to_connection( "node11", "node21"), 
        to_connection( "node21", "node31"), 
        to_connection( "node31", "node41"), 
        to_connection( "node41", "node51"), 
        to_connection( "node51", "node61"), 
        to_connection( "node61", "node71"), 

        to_connection( "input1", "node11","north","south"), 
        to_connection( "input2", "node21","north","south"), 
        to_connection( "input3", "node31","north","south"), 
        to_connection( "input4", "node41","north","south"), 
        to_connection( "input5", "node51","north","south"), 
        to_connection( "input6", "node61","north","south"), 
        to_connection( "input7", "node71","north","south"), 

        # 第二层
        to_Cascade("node12", 1, 16,1, offset="(0,10,0)", to="(node11-north)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node22", 1, 16,1, offset="(20,0,0)", to="(node12-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node32", 1, 16,1, offset="(20,0,0)", to="(node22-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node42", 1, 16,1, offset="(20,0,0)", to="(node32-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node52", 1, 16,1, offset="(20,0,0)", to="(node42-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node62", 1, 16,1, offset="(20,0,0)", to="(node52-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node72", 1, 16,1, offset="(20,0,0)", to="(node62-east)", height=5, depth=32, width=5,caption=''),

        to_connection( "node12", "node22"), 
        to_connection( "node22", "node32"), 
        to_connection( "node32", "node42"), 
        to_connection( "node42", "node52"), 
        to_connection( "node52", "node62"), 
        to_connection( "node62", "node72"), 

        to_connection( "node11", "node12","north","south"), 
        to_connection( "node21", "node22","north","south"), 
        to_connection( "node31", "node32","north","south"), 
        to_connection( "node41", "node42","north","south"), 
        to_connection( "node51", "node52","north","south"), 
        to_connection( "node61", "node62","north","south"), 
        to_connection( "node71", "node72","north","south"), 

        # 第三层
        to_Cascade("node13", 1, 16,1, offset="(0,10,0)", to="(node12-north)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node23", 1, 16,1, offset="(20,0,0)", to="(node13-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node33", 1, 16,1, offset="(20,0,0)", to="(node23-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node43", 1, 16,1, offset="(20,0,0)", to="(node33-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node53", 1, 16,1, offset="(20,0,0)", to="(node43-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node63", 1, 16,1, offset="(20,0,0)", to="(node53-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node73", 1, 16,1, offset="(20,0,0)", to="(node63-east)", height=5, depth=32, width=5,caption=''),

        to_connection( "node13", "node23"), 
        to_connection( "node23", "node33"), 
        to_connection( "node33", "node43"), 
        to_connection( "node43", "node53"), 
        to_connection( "node53", "node63"), 
        to_connection( "node63", "node73"), 

        to_connection( "node12", "node13","north","south"), 
        to_connection( "node22", "node23","north","south"), 
        to_connection( "node32", "node33","north","south"), 
        to_connection( "node42", "node43","north","south"), 
        to_connection( "node52", "node53","north","south"), 
        to_connection( "node62", "node63","north","south"), 
        to_connection( "node72", "node73","north","south"), 

        # 全连接层
        to_SoftMax("softMax", 1 ,2,1, offset="(0,10,0)", to="(node73-north)", height=4, depth=6, width=4, caption="SoftMax"  ),
        to_connection( "node73", "softMax","north","south"), 

        to_end()
        ]
    to_generate(arch, os.getcwd()+'\\draw_houyi\\Net26\\Net26.tex' )
    # end draw_Net26


def draw_Net27():
    arch = [
        to_head( '..' ),
        to_cor(),
        to_begin(),

        # 输入层
        to_Conv("input1", 1, 224,1, offset="(0,0,0)", to="(0,0,0)", height=5, depth=224, width=5,caption='frame1'),
        to_Conv("input2", 1, 224,1, offset="(20,0,0)", to="(input1-east)", height=5, depth=224, width=5,caption='frame2'),
        to_Conv("input3", 1, 224,1, offset="(20,0,0)", to="(input2-east)", height=5, depth=224, width=5,caption='frame3'),
        to_Conv("input4", 1, 224,1, offset="(20,0,0)", to="(input3-east)", height=5, depth=224, width=5,caption='frame4'),
        to_Conv("input5", 1, 224,1, offset="(20,0,0)", to="(input4-east)", height=5, depth=224, width=5,caption='frame5'),
        to_Conv("input6", 1, 224,1, offset="(20,0,0)", to="(input5-east)", height=5, depth=224, width=5,caption='frame6'),
        to_Conv("input7", 1, 224,1, offset="(20,0,0)", to="(input6-east)", height=5, depth=224, width=5,caption='frame7'),
        
        # 第一层
        to_Cascade("node11", 1, 16,1, offset="(0,20,0)", to="(input1-north)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node21", 1, 16,1, offset="(20,0,0)", to="(node11-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node31", 1, 16,1, offset="(20,0,0)", to="(node21-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node41", 1, 16,1, offset="(20,0,0)", to="(node31-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node51", 1, 16,1, offset="(20,0,0)", to="(node41-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node61", 1, 16,1, offset="(20,0,0)", to="(node51-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node71", 1, 16,1, offset="(20,0,0)", to="(node61-east)", height=5, depth=32, width=5,caption=''),
        
        to_connection( "node11", "node21"), 
        to_connection( "node21", "node31"), 
        to_connection( "node31", "node41"), 
        to_connection( "node41", "node51"), 
        to_connection( "node51", "node61"), 
        to_connection( "node61", "node71"), 

        to_connection( "input1", "node11","north","south"), 
        to_connection( "input2", "node21","north","south"), 
        to_connection( "input3", "node31","north","south"), 
        to_connection( "input4", "node41","north","south"), 
        to_connection( "input5", "node51","north","south"), 
        to_connection( "input6", "node61","north","south"), 
        to_connection( "input7", "node71","north","south"), 

        # 第二层
        to_Cascade("node12", 1, 16,1, offset="(0,10,0)", to="(node11-north)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node22", 1, 16,1, offset="(20,0,0)", to="(node12-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node32", 1, 16,1, offset="(20,0,0)", to="(node22-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node42", 1, 16,1, offset="(20,0,0)", to="(node32-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node52", 1, 16,1, offset="(20,0,0)", to="(node42-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node62", 1, 16,1, offset="(20,0,0)", to="(node52-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node72", 1, 16,1, offset="(20,0,0)", to="(node62-east)", height=5, depth=32, width=5,caption=''),

        to_connection( "node12", "node22"), 
        to_connection( "node22", "node32"), 
        to_connection( "node32", "node42"), 
        to_connection( "node42", "node52"), 
        to_connection( "node52", "node62"), 
        to_connection( "node62", "node72"), 

        to_connection( "node11", "node12","north","south"), 
        to_connection( "node21", "node22","north","south"), 
        to_connection( "node31", "node32","north","south"), 
        to_connection( "node41", "node42","north","south"), 
        to_connection( "node51", "node52","north","south"), 
        to_connection( "node61", "node62","north","south"), 
        to_connection( "node71", "node72","north","south"), 

        # 第三层
        to_Cascade("node13", 1, 16,1, offset="(0,10,0)", to="(node12-north)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node23", 1, 16,1, offset="(20,0,0)", to="(node13-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node33", 1, 16,1, offset="(20,0,0)", to="(node23-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node43", 1, 16,1, offset="(20,0,0)", to="(node33-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node53", 1, 16,1, offset="(20,0,0)", to="(node43-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node63", 1, 16,1, offset="(20,0,0)", to="(node53-east)", height=5, depth=32, width=5,caption=''),
        to_Cascade("node73", 1, 16,1, offset="(20,0,0)", to="(node63-east)", height=5, depth=32, width=5,caption=''),

        to_connection( "node13", "node23"), 
        to_connection( "node23", "node33"), 
        to_connection( "node33", "node43"), 
        to_connection( "node43", "node53"), 
        to_connection( "node53", "node63"), 
        to_connection( "node63", "node73"), 

        to_connection( "node12", "node13","north","south"), 
        to_connection( "node22", "node23","north","south"), 
        to_connection( "node32", "node33","north","south"), 
        to_connection( "node42", "node43","north","south"), 
        to_connection( "node52", "node53","north","south"), 
        to_connection( "node62", "node63","north","south"), 
        to_connection( "node72", "node73","north","south"), 

        # 全连接层
        to_Sum( "sum", offset="(0,20,0)", to="(node43-north)", radius=2.5, opacity=0.6),
        to_connection( "node13", "sum","north","south"), 
        to_connection( "node23", "sum","north","south"), 
        to_connection( "node33", "sum","north","south"), 
        to_connection( "node43", "sum","north","south"), 
        to_connection( "node53", "sum","north","south"), 
        to_connection( "node63", "sum","north","south"), 
        to_connection( "node73", "sum","north","south"), 


        to_Cascade("cascade", 1,112,1, offset="(0,10,0)", to="(sum-north)", height=5, depth=112, width=5,caption='cascade'),
        to_connection( "sum", "cascade","north","south"), 

        to_FcRelu_fine("fc1", 1, 16,1, offset="(0,10,0)", to="(cascade-north)", height=5, depth=16, width=5,caption='fc1'),
        to_connection( "cascade", "fc1","north","south"), 

        to_SoftMax("softMax", 1 ,2,1, offset="(0,10,0)", to="(fc1-north)", height=3, depth=6, width=3, caption="SoftMax"  ),
        to_connection( "fc1", "softMax","north","south"), 

        to_end()
        ]
    to_generate(arch, os.getcwd()+'\\draw_houyi\\Net27\\Net27.tex' )
    # end draw_Net27



def draw_Net28():
    arch = [
        to_head( '..' ),
        to_cor(),
        to_begin(),

        # 第一帧
        # CNN 模块
        to_Conv("input", 32, 32,3, offset="(0,0,0)", to="(0,0,0)", height=32, depth=32, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=6, height=6),
        
        to_ConvRelu("conv1", 28, 28,6, offset="(3,0,0)", to="(input-east)", height=28, depth=28, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 14,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=14, width=6,caption="AvgPool"),
            
        to_ConvRelu("conv2", 10, 10,8, offset="(2,0,0)", to="(pool1-east)", height=10, depth=10, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool21", 5, 5,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=5, width=8,caption="AvgPool"),
        # LSTM 模块
        to_Conv("input1", 1, 200,1, offset="(5,0,0)", to="(pool21-east)", height=2.5, depth=100, width=2.5,caption='frame1'),
        to_Cascade("node11", 1, 16,1, offset="(6,0,0)", to="(input1-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node21", 1, 16,1, offset="(3,0,0)", to="(node11-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node31", 1, 16,1, offset="(3,0,0)", to="(node21-east)", height=2.5, depth=8, width=2.5,caption=''),
        
        to_connection( "pool21", "input1"), 
        to_connection( "input1", "node11"), 
        to_connection( "node11", "node21"), 
        to_connection( "node21", "node31"), 


        # 第二帧
        # CNN 模块
        to_Conv("input", 32, 32,3, offset="(0,-10,0)", to="(0,0,0)", height=32, depth=32, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=6, height=6),

        to_ConvRelu("conv12", 28, 28,6, offset="(3,0,0)", to="(input-east)", height=28, depth=28, width=6,caption='conv1'),
        to_connection( "input", "conv12"), 
        to_Pool("pool1", 14, 14,6,offset="(0,0,0)", to="(conv12-east)",height=14, depth=14, width=6,caption="AvgPool"),
            
        to_ConvRelu("conv2", 10, 10,8, offset="(2,0,0)", to="(pool1-east)", height=10, depth=10, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool22", 5, 5,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=5, width=8,caption="AvgPool"),
        # LSTM 模块
        to_Conv("input2", 1, 200,1, offset="(5,0,0)", to="(pool22-east)", height=2.5, depth=100, width=2.5,caption='frame1'),
        to_Cascade("node12", 1, 16,1, offset="(6,0,0)", to="(input2-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node22", 1, 16,1, offset="(3,0,0)", to="(node12-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node32", 1, 16,1, offset="(3,0,0)", to="(node22-east)", height=2.5, depth=8, width=2.5,caption=''),
        
        to_connection( "pool22", "input2"), 
        to_connection( "input2", "node12"), 
        to_connection( "node12", "node22"), 
        to_connection( "node22", "node32"), 
        
        to_transNode("transNode11",offset="(0,-4,0)", to="(node12-south)"),
        to_transNode("transNode21",offset="(0,-4,0)", to="(node22-south)"),
        to_transNode("transNode31",offset="(0,-4,0)", to="(node32-south)"),

        to_connection( "node11", "node12","south","north"), 
        to_connection( "node21", "node22","south","north"), 
        to_connection( "node31", "node32","south","north"), 

        to_connection( "node12", "transNode11","south","north"), 
        to_connection( "node22", "transNode21","south","north"), 
        to_connection( "node32", "transNode31","south","north"), 


        # 第七帧
        # CNN 模块
        to_Conv("input", 32, 32,3, offset="(0,-25,0)", to="(0,0,0)", height=32, depth=32, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=6, height=6),
        
        to_ConvRelu("conv17", 28, 28,6, offset="(3,0,0)", to="(input-east)", height=28, depth=28, width=6,caption='conv1'),
        to_connection( "input", "conv17"), 
        to_Pool("pool1", 14, 14,6,offset="(0,0,0)", to="(conv17-east)",height=14, depth=14, width=6,caption="AvgPool"),
        
        to_ConvRelu("conv2", 10, 10,8, offset="(2,0,0)", to="(pool1-east)", height=10, depth=10, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool27", 5, 5,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=5, width=8,caption="AvgPool"),
        # LSTM 模块
        to_Conv("input7", 1, 200,1, offset="(5,0,0)", to="(pool27-east)", height=2.5, depth=100, width=2.5,caption='frame1'),
        to_Cascade("node17", 1, 16,1, offset="(6,0,0)", to="(input7-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node27", 1, 16,1, offset="(3,0,0)", to="(node17-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node37", 1, 16,1, offset="(3,0,0)", to="(node27-east)", height=2.5, depth=8, width=2.5,caption=''),
        
        to_connection( "pool27", "input7"), 
        to_connection( "input7", "node17"), 
        to_connection( "node17", "node27"), 
        to_connection( "node27", "node37"),        
       
        to_transNode("transNode12", offset="(0,4,0)", to="(node17-south)"),
        to_transNode("transNode22", offset="(0,4,0)", to="(node27-south)"),
        to_transNode("transNode32", offset="(0,4,0)", to="(node37-south)"),
        
        to_connection( "transNode12", "node17","south","north"), 
        to_connection( "transNode22", "node27","south","north"), 
        to_connection( "transNode32", "node37","south","north"), 

        # # 省略号
        # to_ellipsis( "conv12", "conv17"),

        # 全连接层
        to_SoftMax("softMax", 1 ,2,1, offset="(3,0,0)", to="(node37-east)", height=2, depth=4, width=2, caption="SoftMax"  ),
        to_connection( "node37", "softMax"), 

        to_end()
        ]
    to_generate(arch, os.getcwd()+'\\draw_houyi\\Net28\\Net28.tex' )
    # end draw_Net28



def draw_Net29():
    arch = [
        to_head( '..' ),
        to_cor(),
        to_begin(),

        # 第一帧
        # CNN 模块        
        to_Conv("input", 32, 96,3, offset="(0,0,0)", to="(0,0,0)", height=32, depth=96, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=18, height=6),
        
        to_ConvRelu("conv1", 28, 82,6, offset="(3,0,0)", to="(input-east)", height=28, depth=82, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 40,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=40, width=6,caption="MaxPool"),
            
        to_ConvRelu("conv2", 10, 26,8, offset="(3,0,0)", to="(pool1-east)", height=10, depth=26, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool2", 5, 12,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=12, width=8,caption="MaxPool"),
        
        to_ConvRelu("conv3", 5, 12,8, offset="(2,0,0)", to="(pool2-east)", height=5, depth=12, width=8,caption='conv3'),
        to_connection( "pool2", "conv3"), 
        to_Pool("pool31", 2, 4,8,offset="(0,0,0)", to="(conv3-east)",height=2, depth=4, width=8,caption="MaxPool"),
        # LSTM 模块
        to_Conv("input1", 1, 64,1, offset="(5,0,0)", to="(pool31-east)", height=2.5, depth=64, width=2.5,caption='frame1'),
        to_Cascade("node11", 1, 8,1, offset="(6,0,0)", to="(input1-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node21", 1, 8,1, offset="(3,0,0)", to="(node11-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node31", 1, 8,1, offset="(3,0,0)", to="(node21-east)", height=2.5, depth=8, width=2.5,caption=''),
        
        to_connection( "pool31", "input1"), 
        to_connection( "input1", "node11"), 
        to_connection( "node11", "node21"), 
        to_connection( "node21", "node31"), 

        # 第二帧
        to_Conv("input", 32, 96,3, offset="(0,15,0)", to="(0,0,0)", height=32, depth=96, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=18, height=6),
        
        to_ConvRelu("conv1", 28, 82,6, offset="(3,0,0)", to="(input-east)", height=28, depth=82, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 40,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=40, width=6,caption="MaxPool"),
            
        to_ConvRelu("conv2", 10, 26,8, offset="(3,0,0)", to="(pool1-east)", height=10, depth=26, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool2", 5, 12,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=12, width=8,caption="MaxPool"),
        
        to_ConvRelu("conv3", 5, 12,8, offset="(2,0,0)", to="(pool2-east)", height=5, depth=12, width=8,caption='conv3'),
        to_connection( "pool2", "conv3"), 
        to_Pool("pool32", 2, 4,8,offset="(0,0,0)", to="(conv3-east)",height=2, depth=4, width=8,caption="MaxPool"),
        # LSTM 模块
        to_Conv("input2", 1, 64,1, offset="(5,0,0)", to="(pool32-east)", height=2.5, depth=64, width=2.5,caption='frame2'),
        to_Cascade("node12", 1, 8,1, offset="(6,0,0)", to="(input2-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node22", 1, 8,1, offset="(3,0,0)", to="(node12-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node32", 1, 8,1, offset="(3,0,0)", to="(node22-east)", height=2.5, depth=8, width=2.5,caption=''),
        
        to_connection( "pool32", "input2"), 
        to_connection( "input2", "node12"), 
        to_connection( "node12", "node22"), 
        to_connection( "node22", "node32"), 

        # 第三帧
        to_Conv("input", 32, 96,3, offset="(0,30,0)", to="(0,0,0)", height=32, depth=96, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=18, height=6),
        
        to_ConvRelu("conv1", 28, 82,6, offset="(3,0,0)", to="(input-east)", height=28, depth=82, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 40,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=40, width=6,caption="MaxPool"),
            
        to_ConvRelu("conv2", 10, 26,8, offset="(3,0,0)", to="(pool1-east)", height=10, depth=26, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool2", 5, 12,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=12, width=8,caption="MaxPool"),
        
        to_ConvRelu("conv3", 5, 12,8, offset="(2,0,0)", to="(pool2-east)", height=5, depth=12, width=8,caption='conv3'),
        to_connection( "pool2", "conv3"), 
        to_Pool("pool33", 2, 4,8,offset="(0,0,0)", to="(conv3-east)",height=2, depth=4, width=8,caption="MaxPool"),
        # LSTM 模块
        to_Conv("input3", 1, 64,1, offset="(5,0,0)", to="(pool33-east)", height=2.5, depth=64, width=2.5,caption='frame3'),
        to_Cascade("node13", 1, 8,1, offset="(6,0,0)", to="(input3-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node23", 1, 8,1, offset="(3,0,0)", to="(node13-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node33", 1, 8,1, offset="(3,0,0)", to="(node23-east)", height=2.5, depth=8, width=2.5,caption=''),
        
        to_connection( "pool33", "input3"), 
        to_connection( "input3", "node13"), 
        to_connection( "node13", "node23"), 
        to_connection( "node23", "node33"), 

        # 第四帧
        to_Conv("input", 32, 96,3, offset="(0,45,0)", to="(0,0,0)", height=32, depth=96, width=3,caption='input'),
        to_input( 'eeg.jpg', to='(input-east)', width=18, height=6),
        
        to_ConvRelu("conv1", 28, 82,6, offset="(3,0,0)", to="(input-east)", height=28, depth=82, width=6,caption='conv1'),
        to_connection( "input", "conv1"), 
        to_Pool("pool1", 14, 40,6,offset="(0,0,0)", to="(conv1-east)",height=14, depth=40, width=6,caption="MaxPool"),
            
        to_ConvRelu("conv2", 10, 26,8, offset="(3,0,0)", to="(pool1-east)", height=10, depth=26, width=8,caption='conv2'),
        to_connection( "pool1", "conv2"), 
        to_Pool("pool2", 5, 12,8,offset="(0,0,0)", to="(conv2-east)",height=5, depth=12, width=8,caption="MaxPool"),
        
        to_ConvRelu("conv3", 5, 12,8, offset="(2,0,0)", to="(pool2-east)", height=5, depth=12, width=8,caption='conv3'),
        to_connection( "pool2", "conv3"), 
        to_Pool("pool34", 2, 4,8,offset="(0,0,0)", to="(conv3-east)",height=2, depth=4, width=8,caption="MaxPool"),
        # LSTM 模块
        to_Conv("input4", 1, 64,1, offset="(5,0,0)", to="(pool34-east)", height=2.5, depth=64, width=2.5,caption='frame4'),
        to_Cascade("node14", 1, 8,1, offset="(6,0,0)", to="(input4-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node24", 1, 8,1, offset="(3,0,0)", to="(node14-east)", height=2.5, depth=8, width=2.5,caption=''),
        to_Cascade("node34", 1, 8,1, offset="(3,0,0)", to="(node24-east)", height=2.5, depth=8, width=2.5,caption=''),
        
        to_connection( "pool34", "input4"), 
        to_connection( "input4", "node14"), 
        to_connection( "node14", "node24"), 
        to_connection( "node24", "node34"), 
        
        # 全连接层
        to_Sum( "sum", offset="(12,7,0)", to="(node32-east)", radius=2.5, opacity=0.6),
        to_connection( "node31", "sum"),
        to_connection( "node32", "sum"),
        to_connection( "node33", "sum"),
        to_connection( "node34", "sum"),

        to_Cascade("cascade", 1, 32,1, offset="(5,0,0)", to="(sum-east)", height=2.5, depth=32, width=2.5,caption='cascade'),
        to_connection( "sum", "cascade"), 


        to_FcRelu_fine("fc", 1, 8,1, offset="(3,0,0)", to="(cascade-east)", height=2.5, depth=12, width=2.5,caption='fc'),
        to_connection( "cascade", "fc"), 


        to_SoftMax("softMax", 1 ,2,1, offset="(3,0,0)", to="(fc-east)", height=2, depth=4, width=2, caption="SoftMax"  ),
        to_connection( "fc", "softMax"), 

        to_end()
        ]
    to_generate(arch, os.getcwd()+'\\draw_houyi\\Net29\\Net29.tex' )
    # end draw_Net29



# 四分类
# draw_Net4()
# draw_Net42()
# draw_Net45()
# draw_Net46()
# draw_Net47()
# draw_Net48()
# draw_Net49()

# 二分类
# draw_Net2()
# draw_Net22()
# draw_Net23()
draw_Net24()
# draw_Net25()
# draw_Net26()
# draw_Net27()
# draw_Net28()
# draw_Net29()