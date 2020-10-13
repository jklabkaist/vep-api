# from django.test import TestCase
from unittest import TestCase, main

# Create your tests here.
import sys, os
sep = os.path.sep

# print( )
module_path = os.path.dirname(os.path.abspath(__file__) )+sep+".."+sep+"modules"+sep
print("module_path :",module_path)
sys.path.append(module_path)
import seq_processor as sp
def unitTest():
    mes3_str = 'TTTCTGTGTCCTTCCTCCAACCC'
    print("==get_mes3==")
    print("input  : ",mes3_str)
    # print("output : ",sp.get_mes3(mes3_str))
    print("="*10)

    test_str ="GCACCAAAGGAGGAAATCTGCCTGCATGATCCAATCACCTCCCATCAGGCCCCACCTCCAACATTGGGTATT"
    print("==get_hexamer_track_info==")
    print("input",test_str)
    print("output ",sp.get_hexamer_track_info(test_str)['5p_exon'])
    print("="*10)


    region_str ='chr14,31549779,31549850,+'
    print("==get_position_to_seq==")
    print("input ",region_str)
    print("output ",sp.get_position_To_seq(region_str))
    print("="*10)
def test_get_hexamer_maxent1():
    print("get_hexamer_maxent1 TEST (SNP)")
    snv_re = sp.get_hexamer_maxent1("11:108236168 A>C")
    print(snv_re)

    print("get_hexamer_maxent1 TEST (indel)")
    indel_re = sp.get_hexamer_maxent1("11:108236165 TTCAG>T")
    print(indel_re)
if __name__ == '__main__':
    test_get_hexamer_maxent1()
    # unitTest()