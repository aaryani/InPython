from tardis.DEF_CALL.metamodelling import echo_module

from tardis import counting_t
echo_module(counting_t)
from tardis.counting_t import mod1
echo_module(mod1)
from tardis.counting_t.mod1 import mod11
echo_module(mod11)
from tardis.counting_t import mod2
echo_module(mod2)
from tardis.counting_t import A
echo_module(A)
from tardis.counting_t import B
echo_module(B)
from tardis.counting_t import Private_mod
echo_module(Private_mod)
