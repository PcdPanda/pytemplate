cdef class CythonClass:
    def __cinit__(self, const double x):
        self.x = x

    cdef void cprint(self) noexcept:
        print('print')
    
    def print(self):
        self.cprint()

    cpdef double python_print(self):
        return self.x