#导入hashlib模块
import hashlib

#获取一个md5的加密算法的对象
md =hashlib.md5()
#制定需要加密的字符串
#hashlib是对二进制进行加密的，不能直接对字符串加密。因此需要通过encode将字符串转码成二进制格式
md.update('how to use md5 in hashlib?'.encode('utf-8'))
#获取加密后的十六进制字符串
print(md.hexdigest())