# Test documentation CMakeLists.txt
project(HelloWorldDoc)

# This variable should be provided by the top-level CMakeLists.txt
set(RELEASE_VERSION v0.0)

###############################################################################
# Variables
###############################################################################

# Doxygen #####################################################################

set(DOXYGEN_INPUT Doxyfile)
set(DOXYGEN_OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile)

set(DOXYGEN_INPUT_DIR ${SRC_DIR})
set(DOXYGEN_EXAMPLES_DIR ${EXAMPLES_DIR})
set(DOXYGEN_MARKDOWN_DIR ${PROJECT_SOURCE_DIR}/doxmd)
set(DOXYGEN_OUTDIR ${PROJECT_BINARY_DIR}/xml)

# Bytefield ###################################################################

set(BYTEFIELD_EXECUTABLE
    ${PROJECT_BINARY_DIR}/node_modules/bytefield-svg/cli.js)

set(BYTEFIELD_SOURCEDIR ${PROJECT_SOURCE_DIR}/bytefield)
set(BYTEFIELD_BUILDDIR ${PROJECT_SOURCE_DIR}/source/bytefields)

# Sphinx ######################################################################

set(SPHINX_SOURCE_DIR ${PROJECT_SOURCE_DIR}/source)
set(SPHINX_EXT_DIR ${SPHINX_SOURCE_DIR}/_ext)
set(SPHINX_HTML_STATIC_PATH ${SPHINX_SOURCE_DIR}/_static)
set(SPHINX_TEMPLATES_PATH ${SPHINX_SOURCE_DIR}/_templates)
set(SPHINX_XML_DIR ${DOXYGEN_OUTDIR})
set(SPHINX_CONFIG_FILE_OUT ${PROJECT_BINARY_DIR}/conf.py)

###############################################################################
# Packages
###############################################################################

find_package(Doxygen REQUIRED)
find_package(Python COMPONENTS Interpreter REQUIRED)

find_program(NPM_EXECUTABLE NAMES npm HINTS /usr REQUIRED)
find_program(SPHINX_BUILD_EXECUTABLE NAMES sphinx-build HINTS /usr REQUIRED)

###############################################################################
# Preprocess/copy files
###############################################################################

# Preprocess Doxyfile
configure_file(${DOXYGEN_INPUT} ${DOXYGEN_OUTPUT} @ONLY)
# Preprocess conf.py
configure_file(${SPHINX_SOURCE_DIR}/conf.py.in ${SPHINX_CONFIG_FILE_OUT} @ONLY)

# Copy package.json and package-lock.json to builddir as bytefield-svg will be
# installed there
file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/package-lock.json
    DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/package.json
    DESTINATION ${CMAKE_CURRENT_BINARY_DIR})

###############################################################################
# Targets
###############################################################################

add_custom_target(GenerateXML ALL
    COMMAND ${DOXYGEN_EXECUTABLE} ${DOXYGEN_OUTPUT}
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    COMMENT "Generating XML"
    VERBATIM
    USES_TERMINAL
)

add_custom_target(InstallBytefield ALL
    COMMAND ${NPM_EXECUTABLE} ci
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    COMMENT "Installing bytefield-svg"
    VERBATIM
    USES_TERMINAL
)

add_custom_target(GenerateSVG ALL
    COMMAND make svg
        BYTEFIELD=${BYTEFIELD_EXECUTABLE}
        SOURCEDIR=${BYTEFIELD_SOURCEDIR}
        BUILDDIR=${BYTEFIELD_BUILDDIR}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
    DEPENDS InstallBytefield
    COMMENT "Generating SVG bytefield diagrams"
    VERBATIM
    USES_TERMINAL
)

add_custom_target(GenerateHTML ALL
    COMMAND ${SPHINX_BUILD_EXECUTABLE} -M html ${SPHINX_SOURCE_DIR}
        ${PROJECT_BINARY_DIR} -c ${PROJECT_BINARY_DIR}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
    DEPENDS GenerateXML
    COMMENT "Generating HTML"
    VERBATIM
    USES_TERMINAL
)

add_custom_target(TouchNojekyll ALL
    COMMAND ${CMAKE_COMMAND} -E touch .nojekyll
    WORKING_DIRECTORY ${PROJECT_BINARY_DIR}/html
    COMMENT "Create .nojekyll file"
    VERBATIM
    USES_TERMINAL
)
