include_directories(
    ${CMAKE_SOURCE_DIR}/src
    ${CMAKE_CURRENT_BINARY_DIR}
)

set(JoineryGui_LIBS
    Joinery
    FreeCADGui
)

qt_add_resources(Joinery_QRC_SRCS Resources/Joinery.qrc)

SET(JoineryGui_SRCS
    ${Joinery_QRC_SRCS}
    AppJoineryGui.cpp
    Command.cpp
    PreCompiled.cpp
    PreCompiled.h
    Workbench.cpp
    Workbench.h
)

add_library(JoineryGui SHARED ${JoineryGui_SRCS})
target_link_libraries(JoineryGui ${JoineryGui_LIBS})

SET_BIN_DIR(JoineryGui JoineryGui /Mod/Joinery)
SET_PYTHON_PREFIX_SUFFIX(JoineryGui)

install(TARGETS JoineryGui DESTINATION ${CMAKE_INSTALL_LIBDIR})
