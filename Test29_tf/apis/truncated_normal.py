'''
tf.truncated_normal
truncated_normal(
    shape,
    mean=0.0,
    stddev=1.0,
    dtype=tf.float32,
    seed=None,
    name=None
)
产生截断正态分布随机数，取值范围为 [ mean - 2 * stddev, mean + 2 * stddev ]。
参数列表：
参数名 	必选 	类型 	说明
shape 	是 	1 维整形张量或 array 	输出张量的维度
mean 	否 	0 维张量或数值 	均值
stddev 	否 	0 维张量或数值 	标准差
dtype 	否 	dtype 	输出类型
seed 	否 	数值 	随机种子，若 seed 赋值，每次产生相同随机数
name 	否 	string 	运算名称

'''
import tensorflow as tf
initial = tf.truncated_normal(shape=[3,3], mean=0, stddev=1)
print(tf.Session().run(initial))
