COMPETITION_ID = 3

COMPETITION_END_DATE = "2025-01-22"

ALLOWED_MODULES = [
    "langchain_community",
    "langchain_openai",
    "ast",
    "sentence_transformers",
    "networkx",
    "grep_ast",
    "tree_sitter",
    "tree_sitter_languages", 
    "rapidfuzz",
    "llama_index",
    "pydantic",
    "numpy",
    "ruamel.yaml",
    "json",
    "libcst",
    "schemas.swe",
    "abc",
    "coding.finetune.llm.client",
    "coding.schemas.swe",
    "requests",
    "difflib",
    "logging",
    "time",
    "datetime",
    "random",
    "sklearn",
    "argparse",
    "uuid",
    "pandas",
    "numpy",
    "tqdm",
    "collections",
    "platform",
    "re",
    "traceback",
    "typing",
    "resource",
    "concurrent",
    "io",
    "tokenize",
    "pathlib",
    "threading",
    "jsonlines",
    "tiktoken",
    "openai",
    "anthropic"
]

ALLOWED_IMPORTS = {
    'os': ['getenv', 'path', 'environ', 'makedirs', 'rm', 'walk', 'sep', 'remove'],
}

NUM_ALLOWED_CHARACTERS = 1000000
