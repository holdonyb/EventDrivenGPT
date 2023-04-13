from .end_user import EndUser
from .project_manager import ProjectManager
from .product_manager import ProductManager
from .programmer import Programmer
from .debugger import Debugger
from .tester import Tester
from .executor import Executor

end_user = EndUser()
project_manager = ProjectManager()
product_manager = ProductManager()
programmer = Programmer()
debugger = Debugger()
tester = Tester()
executor = Executor()

project_manager.init_roles(end_user, product_manager, programmer, debugger, tester, executor)
