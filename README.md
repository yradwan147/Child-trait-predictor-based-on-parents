# Child trait predictor based on parents

Predicts mendellian child traits using phenotype inputs from 2 parents.
GUI created used PySimpleGUI
The application includes 2 input panels: one for parent 1 and one for parent 2.

After the user inputs the phenotypes of both parents, the application calculates all possible genotypes for the child and outputs them in image form in a separate output panel on the right.
The output includes a visual representation of the child (his phenotype), in addition to the probability of this specific possibility and his genotype as text under the image. Users can scroll through the results using the forward and back buttons and they can submit new inputs using the submit button.
The application programming logic uses simple Mendellian trait methodology with the noted info that if a dominant trait is inputted into the application, the application proposes a 50/50 chance of either a homozygous dominant genotype or a heterozygous genotype.
After the application decides the phenotypes for each trait, it builds the face by overlapping transparent images of each trait, thus forming the full face.

All assets and art in the application were created uniquely with the help of Pixel Artist Saif Tarek (referenced in acknowledgments)
