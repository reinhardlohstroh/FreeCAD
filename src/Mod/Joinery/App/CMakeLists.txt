set(Joinery_LIBS
    FreeCADApp
)

SET(Joinery_SRCS
    AppJoinery.cpp
    PreCompiled.cpp
    PreCompiled.h
)

add_library(Joinery SHARED ${Joinery_SRCS})
target_link_libraries(Joinery ${Joinery_LIBS})


SET_BIN_DIR(Joinery Joinery /Mod/Joinery)
SET_PYTHON_PREFIX_SUFFIX(Joinery)

install(TARGETS Joinery DESTINATION ${CMAKE_INSTALL_LIBDIR})
