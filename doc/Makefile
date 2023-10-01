SOURCEDIR     ?= source
BUILDDIR      ?= build

BYTEFIELD     ?= bytefield-svg

BYTEFIELD_IN = $(wildcard $(SOURCEDIR)/*.clj)
BYTEFIELD_OUT = $(subst $(SOURCEDIR),$(BUILDDIR),$(BYTEFIELD_IN))
BYTEFIELD_SVG = $(subst clj,svg,$(BYTEFIELD_OUT))

# bytefield targets

svg: $(BYTEFIELD_SVG)

$(BUILDDIR)/%.svg: $(SOURCEDIR)/%.clj
	$(BYTEFIELD) <$< >$@
