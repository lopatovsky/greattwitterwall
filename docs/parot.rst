The parrot module
=================

.. testsetup::

   class Parrot:
       def voom(self, voltage):
           print('This parrot wouldn\'t voom if you put {} volts through it!'.format(voltage))

       def die(self):
           return 'RIP'


   parrot = Parrot()

The parrot module is a module about parrots.

Doctest example:

.. doctest::

   >>> parrot.voom(3000)
   This parrot wouldn't voom if you put 3000 volts through it!

Test-Output example:

.. testcode::

   parrot.voom(3000)

This would output:

.. testoutput::

   This parrot wouldn't voom if you put 3000 volts through it!

You can use other values:

.. testcode::

   parrot.voom(230)

.. testoutput::
   :hide:

   This parrot wouldn't voom if you put 230 volts through it!


.. testcleanup::

   parrot.die()
