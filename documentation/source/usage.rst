Usage
=====

This section describes how to approach the agentic-backbone project and the expected workflows.

Running the project
-------------------

This repository currently contains documentation scaffolding and project metadata.
As the agentic-backbone implementation matures, add runtime instructions here.

Recommended structure
---------------------

- ``agentic-skills``: skill modules for individual agent roles.
- ``agentic-memory``: persistent storage for long-lived agent context.
- ``swarm runner``: orchestration layer that starts and supervises multiple agents.

Documentation contributions
---------------------------

To add or update guidance, edit the corresponding ``.rst`` file in ``documentation/source``.
Then rebuild the docs with:

.. code-block:: console

   make html

If you want to add API documentation later, use the built-in Sphinx ``autodoc`` extension and document Python modules with docstrings.
