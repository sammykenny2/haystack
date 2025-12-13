# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Haystack is an end-to-end LLM framework by deepset for building applications powered by LLMs, Transformer models, and vector search. It enables RAG, document search, question answering, and complex query resolution through modular pipelines.

## Development Commands

### Environment Setup
```bash
# Install Hatch (project manager) first - see https://hatch.pypa.io/latest/install/
hatch shell              # Create and enter virtual environment
pre-commit install       # Set up pre-commit hooks
```

### Running Tests
```bash
hatch run test:unit      # Run all unit tests
hatch run test:unit test/path/to/test.py::TestClass::test_method  # Run specific test
hatch run test:integration  # Run all integration tests
hatch run test:integration-only-fast  # Skip slow integration tests
hatch run test:integration-only-slow  # Run only slow tests
```

### Code Quality
```bash
hatch run fmt            # Format code and fix lint issues (ruff)
hatch run fmt-check      # Check formatting without fixing
hatch run test:types     # Run mypy type checking
hatch run test:lint      # Run pylint
```

### Release Notes
```bash
hatch run release-note <note-name>  # Create release note file in releasenotes/notes/
```

## Architecture

### Core Concepts

**Components** (`haystack/core/component/`): Building blocks decorated with `@component`. Each component:
- Must have a `run()` method (mandatory)
- May have `warm_up()` for heavy initialization (called before pipeline execution)
- Has automatically serialized `init_parameters` for save/load
- Uses `InputSocket` and `OutputSocket` for typed connections

**Pipelines** (`haystack/core/pipeline/`): Orchestration engine connecting components:
- `Pipeline` - synchronous execution
- `AsyncPipeline` - async execution
- `PipelineBase` - shared base functionality
- Components connect via `pipeline.connect("source.output", "target.input")`

**SuperComponent** (`haystack/core/super_component/`): Wraps a Pipeline to act as a single component, enabling nested pipelines.

### Package Structure

- `haystack/components/` - All built-in components organized by function:
  - `agents/` - Agent components with state management
  - `builders/` - PromptBuilder, ChatPromptBuilder, AnswerBuilder
  - `converters/` - Document converters (PDF, DOCX, HTML, Markdown, etc.)
  - `embedders/` - OpenAI, HuggingFace, SentenceTransformers embedders
  - `generators/` - LLM generators (OpenAI, HuggingFace, Azure)
  - `retrievers/` - Document retrieval components
  - `rankers/` - Document ranking components
  - `routers/` - Conditional routing components
  - `preprocessors/` - Document cleaning and splitting
  - `writers/` - Document store writers

- `haystack/dataclasses/` - Core data types: `Document`, `ChatMessage`, `Answer`, `ByteStream`, `StreamingChunk`

- `haystack/document_stores/` - Document storage abstractions (InMemory implementation; others in haystack-core-integrations)

- `haystack/tools/` - Tool definitions for function calling

- `haystack/tracing/` - OpenTelemetry and ddtrace integration

### Testing Structure

- `test/` mirrors `haystack/` structure
- Tests use pytest markers: `@pytest.mark.unit`, `@pytest.mark.integration`, `@pytest.mark.slow`
- Integration tests may require external services (Docker containers, API keys)

## Key Patterns

### Creating a Component
```python
from haystack import component

@component
class MyComponent:
    def __init__(self, param: str):
        # Keep __init__ lightweight; heavy init goes in warm_up()
        pass

    def warm_up(self):
        # Called once before pipeline runs; load models here
        pass

    @component.output_types(result=str)
    def run(self, input_data: str) -> dict[str, str]:
        return {"result": processed_data}
```

### Pipeline Construction
```python
from haystack import Pipeline

pipeline = Pipeline()
pipeline.add_component("name", component_instance)
pipeline.connect("source_component.output", "target_component.input")
result = pipeline.run({"component_name": {"input_name": value}})
```

## PR Requirements

- Use conventional commit format for PR titles
- Create release notes with `hatch run release-note <name>` (required unless labeled `ignore-for-release-notes`)
- Release notes use reStructuredText formatting with double backticks for inline code
