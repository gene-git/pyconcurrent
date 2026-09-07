
========
Examples
========


Examples running an executable synchronously, using multiprocessing and using asyncio.
These use:

* ProcRunAsyncio class
* ProcRunMp class
* run_prog

along with ProcResult class.

Example 1a: Executable with Asyncio
-----------------------------------

This example uses asyncio and subprocesses to call an executable.
*tasks* must be a list of *(key, arg)* pairs, 1 per task.

*key* is a unique identifier, used by caller, one per task. *arg* is an additional argument
for each task; typically *arg* provides for whatever work that task is responsible for.
Each *result* returned contains both the *key* and the *arg* used by that task,
information about the success of the task as well as any outputs produced by the task.
See *ProcResult* class for more detail.

This example has 5 tasks to be run concurrently, at most 4 at a time. The results are
available in the *proc_run.result*, which is a list of *ProcResult* items; one per task.
Since the result order is not pre-defined, each task is identifiable by it's *key* available
in the : *result.key*.

.. literalinclude:: examples/example_1a.py
   :language: python
   :caption: Example 1a

Example 1b: Executable with Multiprocessing
-------------------------------------------

To switch to *multiprocessing* simply replace *ProcRunAsyncio* with  *ProcRunMp*,
and drop *await* since MP is not *async*. i.e.

.. literalinclude:: examples/example_1b.py
   :language: python
   :caption: Example 1b

Example 2: Function with Asnycio
--------------------------------

The next example uses a caller supplied function together with asyncio. As in the first
example, there are 5 tasks to do and the number of workers is 4, so that 4 tasks
are permitted to be run simultaneously.

.. literalinclude:: examples/example_2.py
   :language: python
   :caption: Example 2

For equivalent multiprocessor version for this one, same as above, simply replace *ProcRunAsyncio*
with *ProcRunMp* and drop any references to **async/await**.

The caller supplied function here, *test_func_async()*, must return a 2-tuple
of *(success:bool, answer:Any)* where success should be *True* if function succeeded.

The function may optionally raise a *RuntimeError* exception, but typically setting *success*
is sufficient. If you are using exceptions then please use this one.


Example 3: Executable with run_prog
-----------------------------------

This example illustrates a non-concurrent external program being executed.

.. literalinclude:: examples/example_3.py
   :language: python
   :caption: Example 3


