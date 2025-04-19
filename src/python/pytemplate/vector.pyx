from libcpp.vector cimport vector
from libcpp.string cimport string


cpdef vec():
    cdef vector[string] v
    v.push_back(string(b'vec'))
    print(v[0].c_str())
