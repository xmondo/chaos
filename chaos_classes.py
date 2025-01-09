class ChaosFunctionsMultiExponent:
    def __init__(self, q, p1, p2, amplitude):
        self.p1 = p1
        self.p2 = p2
        self.amplitude = amplitude
        self.q = q

    # trigonometric chaos functions
    def cos_sin_1(self):
        import numpy as np
        _cos_sin_1 = self.amplitude * np.cos(1 / (0.01 + self.q) ** self.p1) * np.sin(1 / (0.01 + self.q) ** self.p2)
        _color = "orangered"
        _label = str(r'$\frac{1}{cos(q^{p_1})sin(q^{p_{2}})}$')
        _power1 = str(self.p1)
        _power2 = str(self.p2)
        return _cos_sin_1, _color, _label, _power1, _power2

    def cos_sin_2(self):
        import numpy as np
        _cos_sin_1 = self.amplitude * np.cos(1 / (0.01 + self.q) ** self.p1) * np.sin(1 / (1 - self.q** self.p2 + 0.01) )
        _color = "red"
        _label = str(r'$\frac{1}{cos^{p_1}(q)}\frac{1}{sin(1 - q^{p_2})}$')
        _power1 = str(self.p1)
        _power2 = str(self.p2)
        return _cos_sin_1, _color, _label, _power1, _power2

class ChaosFunctions:
    def __init__(self, q, p1, amplitude):
        self.p1 = p1
        self.amplitude = amplitude
        self.q = q

    def cos_1(self):
        import numpy as np
        _color = "dodgerblue"
        _label = str(r'$\frac{1}{cos(q^p)}$')
        _power1 = str(self.p1)
        _power2 = 0
        _cos_1 = self.amplitude * np.cos(1 / ((0.01 + self.q) ** self.p1))
        return _cos_1, _color, _label, _power1, _power2

    def sin_1(self):
        import numpy as np
        _color = "royalblue"
        _label = str(r'$\frac{1}{sin(q^p)}$')
        _power1 = str(self.p1)
        _power2 = 0
        _sin_1 = self.amplitude * np.sin(1 / ((0.01 + self.q) ** self.p1))
        return _sin_1, _color, _label, _power1, _power2

    def sin_2(self):
        import numpy as np
        _color = "royalblue"
        _label = str(r'$\frac{3}{sin(q^p)}\frac{5}{(1 - sin(q^p))}$')
        _power1 = str(self.p1)
        _power2 = 0
        _sin_2 = self.amplitude * np.sin(3 / (0.01 + self.q))**self.p1*np.sin(5 / ((1 - self.q + 0.01) ** self.p1))
        return _sin_2, _color, _label, _power1, _power2

class SincFunction:
    def __init__(self, q, p1, amplitude):
        self.p1 = p1
        self.amplitude = amplitude
        self.q = q
    def sinc(self):
        import numpy as np
        _color = "royalblue"
        _power1 = str(self.p1)
        _label = str(r'$\frac{sin(q)}{q}$')
        _sinc = self.amplitude*np.sin(np.pi*self.q * self.p1)/(np.pi * self.q * self.p1)
        return _sinc, _color, _label, _power1, 1
