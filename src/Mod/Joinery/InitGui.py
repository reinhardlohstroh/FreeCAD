# Joinery gui init module
# (c) 2001 Juergen Riegel LGPL


class JoineryWorkbench(Workbench):
    "Joinery workbench object"

    MenuText = "Joinery"
    ToolTip = "Joinery workbench"

    def Initialize(self):
        # load the module
        import JoineryGui

    def GetClassName(self):
        return "JoineryGui::Workbench"


Gui.addWorkbench(JoineryWorkbench())
