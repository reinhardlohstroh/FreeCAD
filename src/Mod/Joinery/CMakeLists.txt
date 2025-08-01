
add_subdirectory(App)
if(BUILD_GUI)
    add_subdirectory(Gui)
endif(BUILD_GUI)

set(Joinery_Scripts
    Init.py
)

if(BUILD_GUI)
    list (APPEND Joinery_Scripts InitGui.py)
endif(BUILD_GUI)

add_custom_target(JoineryScripts ALL
    SOURCES ${Joinery_Scripts}
)

fc_target_copy_resource_flat(JoineryScripts
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_BINARY_DIR}/Mod/Joinery
    ${Joinery_Scripts}
)

install(
    FILES
        ${Joinery_Scripts}
    DESTINATION
        Mod/Joinery
)
