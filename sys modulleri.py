import sys


print(sys.argv)

print("+"*50)

print(len(sys.argv))


//////////////////////////////////////////////////////////////////////////////

"""
Eğer, yazdığınız bir programda, programınızın çalıştığı sistemdeki Python’ın çalıştırılabilir
dosyasının adını ve yolunu öğrenmeniz gerekirse bu niteliği kullanabilirsiniz:

"""
import sys

print(sys.executable)

"""
çıktısı : /usr/bin/python3.5
"""



//////////////////////////////////////////////////////////////////////////////


"""
sys modülünün prefix niteliği Python’ın hangi dizine kurulduğunu gösterir:
"""
import  sys

print(sys.prefix)


//////////////////////////////////////////////////////////////////////////////


"""
sys modülünün version_info niteliği de kullandığınız Python sürümüne ilişkin bilgi verir:
"""
import sys

print(sys.version_info)

"""
çıktısı  :   sys.version_info(major=3, minor=5, micro=2, releaselevel='final', serial=0)
"""


//////////////////////////////////////////////////////////////////////////////


"""
sys modülünün version niteliği kullandığınız Python sürümüne ilişkin ayrıntılı bilgi verir:
"""
import sys

print(sys.version)

"""
çıktısı  :   3.5.2 (default, Sep  2 2016, 03:59:43)
             [GCC 6.1.0]
"""
