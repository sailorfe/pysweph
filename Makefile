clean:
	rm -rf src/swisseph/__pycache__

werk:
	nvim src/libswe/swephexp.h src/build_bridge.py src/swisseph/api.py

# DOCS

BUILD_DIR := docs/_build
SPHINX_SOURCE_DIR := docs/

clean-docs:
	rm -rf $(BUILD_DIR)

docs: clean-docs
	uv run sphinx-build -b html $(SPHINX_SOURCE_DIR) $(BUILD_DIR)

live: clean-docs
	uv run sphinx-autobuild --host 0.0.0.0 $(SPHINX_SOURCE_DIR) $(BUILD_DIR) --watch $(SPHINX_SOURCE_DIR)
