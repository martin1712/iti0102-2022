"""Alchemy."""
import collections


class AlchemicalElement:
    """
    AlchemicalElement class.

    Every element must have a name.
    """

    def __init__(self, name: str):
        """Name for element."""
        self.name = name

    def __repr__(self):
        """How to represent an element."""
        return f"<AE: {self.name}>"


class AlchemicalStorage:
    """AlchemicalStorage class."""

    def __init__(self):
        """
        Initialize the AlchemicalStorage class.

        You will likely need to add something here, maybe a list?
        """
        self.elements = []

    def add(self, element: AlchemicalElement):
        """
        Add element to storage.

        Check that the element is an instance of AlchemicalElement, if it is not, raise the built-in TypeError exception.

        :param element: Input object to add to storage.
        """
        if isinstance(element, AlchemicalElement):
            self.elements.append(element)
        else:
            raise TypeError

    def pop(self, element_name: str) -> AlchemicalElement or None:
        """
        Remove and return previously added element from storage by its name.

        If there are multiple elements with the same name, remove only the one that was added most recently to the
        storage. If there are no elements with the given name, do not remove anything and return None.

        :param element_name: Name of the element to remove.
        :return: The removed AlchemicalElement object or None.
        """
        for element in reversed(self.elements):
            if element.name == element_name:
                self.elements.remove(element)
                return element
        return None

    def extract(self) -> list[AlchemicalElement]:
        """
        Return a list of all of the elements from storage and empty the storage itself.

        Order of the list must be the same as the order in which the elements were added.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            storage.extract() # -> [<AE: Water>, <AE: Fire>]
            storage.extract() # -> []

        In this example, the second time we use .extract() the output list is empty because we already extracted
         everything.

        :return: A list of all of the elements that were previously in the storage.
        """
        out_list = self.elements.copy()
        self.elements.clear()
        return out_list

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the storage.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            print(storage.get_content())

        Output in console:
            Content:
             * Fire x 1
             * Water x 1

        The elements must be sorted alphabetically by name.

        :return: Content as a string.
        """
        result = []
        elements_dict = {}
        for element in self.elements:
            if element.name not in elements_dict:
                elements_dict[element.name] = 1
            else:
                elements_dict[element.name] += 1
        sorted_dict = collections.OrderedDict(sorted(elements_dict.items()))
        for key, value in sorted_dict.items():
            result.append(f" * {key} x {value}")
        if len(result) >= 1:
            return "Content:\n" + "\n".join(result)
        else:
            return "Content:\n Empty."


class AlchemicalRecipes:
    """AlchemicalRecipes class."""

    def __init__(self):
        """
        Initialize the AlchemicalRecipes class.

        Add whatever you need to make this class function.
        """
        self.recipes = []

    def add_recipe(self, first_component_name: str, second_component_name: str, product_name: str):
        """
        Determine if recipe is valid and then add it to recipes.

        A recipe consists of three strings, two components and their product.
        If any of the parameters are the same, raise the 'DuplicateRecipeNamesException' exception.
        If there already exists a recipe for the given pair of components, raise the 'RecipeOverlapException' exception.

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :param product_name: The name of the product element.
        """
        names = []
        if first_component_name == second_component_name or second_component_name == product_name or first_component_name == product_name:
            raise DuplicateRecipeNamesException
        names.append(first_component_name)
        names.append(second_component_name)
        names = sorted(names)
        names.append(product_name)
        for i in self.recipes:
            if names == i:
                raise RecipeOverlapException
            if names[:2] == i[:2] and names[2] != i[2]:
                raise RecipeOverlapException
        self.recipes.append(names)

    def get_product_name(self, first_component_name: str, second_component_name: str) -> str | None:
        """
        Return the name of the product for the two components.

        The order of the first_component_name and second_component_name is interchangeable, so search for combinations
        of (first_component_name, second_component_name) and (second_component_name, first_component_name).

        If there are no combinations for the two components, return None

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            recipes.get_product_name('Water', 'Wind')  # ->  'Ice'
            recipes.get_product_name('Wind', 'Water')  # ->  'Ice'
            recipes.get_product_name('Fire', 'Water')  # ->  None
            recipes.add_recipe('Water', 'Fire', 'Steam')
            recipes.get_product_name('Fire', 'Water')  # ->  'Steam'

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :return: The name of the product element or None.
        """
        for i in self.recipes:
            if first_component_name == i[0] and second_component_name == i[1]:
                return i[2]
            if first_component_name == i[1] and second_component_name == i[0]:
                return i[2]


class DuplicateRecipeNamesException(Exception):
    """Raised when attempting to add a recipe that has same names for components and product."""


class RecipeOverlapException(Exception):
    """Raised when attempting to add a pair of components that is already used for another existing recipe."""


class Cauldron(AlchemicalStorage):
    """
    Cauldron class.

    Extends the 'AlchemicalStorage' class.
    """

    def __init__(self, recipes: AlchemicalRecipes):
        """Initialize the Cauldron class."""
        super().__init__()
        self.recipes = recipes

    def add(self, element: AlchemicalElement):
        """
        Add element to storage and check if it can combine with anything already inside.

        Use the 'recipes' object that was given in the constructor to determine the combinations.

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            cauldron = Cauldron(recipes)
            cauldron.add(AlchemicalElement('Water'))
            cauldron.add(AlchemicalElement('Wind'))
            cauldron.extract() # -> [<AE: Ice>]

        :param element: Input object to add to storage.
        """
        # for i in recipes:
        # for i in cauldron:
        # for i in self.recipes:
        # if element in recipes:
        # if element in cauldron:

        self.elements.append(element.name)
        for i in self.elements:
            result = self.recipes.get_product_name(element.name, i)

            if result:
                super(Cauldron, self).add(AlchemicalElement(result))
        print(self.elements)


if __name__ == '__main__':
    recipes = AlchemicalRecipes()
    recipes.add_recipe('Water', 'Wind', 'Ice')
    recipes.add_recipe('Earth', 'Fire', 'Lava')
    recipes.add_recipe('Water', 'Fire', 'Obsidian')
    cauldron = Cauldron(recipes)
    cauldron.add(AlchemicalElement('Water'))
    cauldron.add(AlchemicalElement('Wind'))
    cauldron.add(AlchemicalElement('Fire'))
    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Fire'))
    cauldron.add(AlchemicalElement('lava'))
    cauldron.extract()  # -> [<AE: Ice>]
