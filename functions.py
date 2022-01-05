from PIL import ImageDraw, Image, ImageFont


def overlap_images(images, prob, genotype):
    prob = str(prob*100)+'%\n'+str(genotype)
    image_1 = Image.open('assets/preview/'+images[0])
    draw = ImageDraw.Draw(image_1)
    w, h = image_1.size
    for image in images:
        image_1.paste(Image.open('assets/preview/'+image),
                      (0, 0), Image.open('assets/preview/'+image))
    # image_1.show()
    font = ImageFont.truetype("arial.ttf", 50)
    text_w, text_h = draw.textsize(str(prob), font)
    draw.text(((w - text_w) // 2, h - text_h-10),
              str(prob), (0, 0, 0), font=font)
    # print(prob)
    return image_1


# image_1 = overlap_images(['dimplen_prev.png', 'earf_prev.png',
#                           'green_prev.png', 'widow_prev.png', 'chin_prev.png'])

# image_1.show()
allele_to_trait = {}
allele_to_trait['CC'] = 'cleft'
allele_to_trait['Cc'] = 'cleft'
allele_to_trait['cc'] = 'smooth'
allele_to_trait['WW'] = 'widow'
allele_to_trait['Ww'] = 'widow'
allele_to_trait['ww'] = 'widown'
allele_to_trait['AA'] = 'attached'
allele_to_trait['Aa'] = 'attached'
allele_to_trait['aa'] = 'free'
allele_to_trait['XX'] = 'duplex'
allele_to_trait['Xx'] = 'duplex'
allele_to_trait['xx'] = 'suplex'
allele_to_trait['DD'] = 'dimple'
allele_to_trait['Dd'] = 'dimple'
allele_to_trait['dd'] = 'dimplen'

trait_to_allele = {v: k for k, v in allele_to_trait.items()}

dominant = ['cleft', 'dimple', 'duplex', 'attached', 'widow']


def allele_gen(a, t):
    if t == 'd':
        return a[0].upper() + a[1].upper()
    elif t == 'h':
        return a[0].upper() + a[1].lower()
    elif t == 'r':
        return a[0].lower() + a[1].lower()


def mendel_calc(prob1, prob2):
    if prob1[0].isupper() and prob2[0].isupper():
        print('here4')
        res = [(prob1[0].upper(), 1)]
        return [[x[0], x[1]*prob1[1]*prob2[1]] for x in res]
        # return [prob1.upper()]
    elif not prob1[0].isupper() and not prob1[0].islower() and not prob2[0].isupper() and not prob2[0].islower():
        res = [(prob1[0].upper(), 0.25), (prob2[0], 0.5),
               (prob1[0].lower(), 0.25)]
        return [[x[0], x[1]*prob1[1]*prob2[1]] for x in res]
        # return[prob1.upper(), prob2, prob1.lower()]
    elif prob1[0].isupper() and not prob2[0].isupper() and not prob2[0].islower():
        res = [(prob2[0].upper(), 0.5), (prob2[0], 0.5)]
        return [[x[0], x[1]*prob1[1]*prob2[1]] for x in res]
        # return[prob2.upper(), prob2]
    elif prob2[0].isupper() and not prob1[0].isupper() and not prob1[0].islower():
        res = [(prob1[0].upper(), 0.5), (prob1[0], 0.5)]
        return [[x[0], x[1]*prob1[1]*prob2[1]] for x in res]
        # return[prob1.upper(), prob1]
    elif prob1[0].islower() and prob2[0].islower():
        res = [(prob1[0], 1)]
        return [[x[0], x[1]*prob1[1]*prob2[1]] for x in res]
        # return [prob1]
    elif prob1[0].isupper() and prob2[0].islower():
        res = [(allele_gen(prob1[0], 'h'), 1)]
        return [[x[0], x[1]*prob1[1]*prob2[1]] for x in res]
        # return [allele_gen(prob1, 'h')]
    elif prob1[0].islower() and not prob2[0].isupper() and not prob2[0].islower():
        res = [(allele_gen(prob1[0].upper(), 'h'), 0.5),
               (prob1[0].lower(), 0.5)]
        return [[x[0], x[1]*prob1[1]*prob2[1]] for x in res]
        # return[allele_gen(prob1.upper(), 'h'), prob1.lower()]
    elif prob2[0].islower() and not prob1[0].isupper() and not prob1[0].islower():
        res = [(allele_gen(prob2[0].upper(), 'h'), 0.5),
               (prob2[0].lower(), 0.5)]
        return [[x[0], x[1]*prob1[1]*prob2[1]] for x in res]
        # return[allele_gen(prob2.upper(), 'h'), prob2.lower()]


def face_gen(widows, ears, eyes, dimples, chins):
    print('Widows: ' + str(widows))
    print('Ears: ' + str(ears))
    print('Eyes: ' + str(eyes))
    print('Dimples: ' + str(dimples))
    print('Chins: ' + str(chins))
    # l11 = input('here')
    faces = []
    faces_img = []
    for widow in widows:
        for ear in ears:
            for eye in eyes:
                for dimple in dimples:
                    for chin in chins:
                        prob = widow[1]*ear[1]*eye[1]*dimple[1]*chin[1]
                        faces.append([[allele_to_trait[widow[0]]+'.png', allele_to_trait[ear[0]]+'.png',
                                     allele_to_trait[eye[0]]+'.png', allele_to_trait[dimple[0]]+'.png', allele_to_trait[chin[0]]+'.png'], prob, widow[0]+ear[0]+eye[0]+dimple[0]+chin[0]])
    # l2 = input(len(faces))
    # faces = set(tuple(x) for x in faces)
    # faces = list(faces)
    # l3 = input(len(faces))
    for face in faces:
        # print(face)
        faces_img.append(overlap_images(face[0], face[1], face[2]))
    # l = input(len(faces_img))
    # for face_img in faces_img:
    #     face_img.show()
    # faces_img[0].show()
    return faces_img


def prob_calc(parent1, parent2):
    res = []
    parent1_probs = []
    parent2_probs = []
    if parent1 in dominant:
        parent1_probs.extend(
            [(allele_gen(trait_to_allele[parent1], 'd'), 0.5), (allele_gen(trait_to_allele[parent1], 'h'), 0.5)])
    elif parent1 not in dominant:
        parent1_probs.extend(
            [(allele_gen(trait_to_allele[parent1], 'r'), 1)])

    if parent2 in dominant:
        parent2_probs.extend(
            [(allele_gen(trait_to_allele[parent2], 'd'), 0.5), (allele_gen(trait_to_allele[parent2], 'h'), 0.5)])
    elif parent2 not in dominant:
        parent2_probs.extend(
            [(allele_gen(trait_to_allele[parent2], 'r'), 1)])
    print('here1')
    for prob1 in parent1_probs:
        for prob2 in parent2_probs:
            print(prob1, prob2)
            print('here2')
            res.extend(mendel_calc(prob1, prob2))
            # l9 = input(res)
            print('here3')
    results_no_dup = {}
    for poss in res:
        results_no_dup[poss[0]] = results_no_dup.get(poss[0], 0)+poss[1]
    new_res = []
    for key, value in results_no_dup.items():
        new_res.append([key, value])
    # l11 = input(new_res)
    # res = set(tuple(x) for x in res)
    # l10 = input(res)
    return (new_res)


# face_gen(prob_calc('widow', 'widow'), prob_calc('attached', 'attached'), prob_calc(
#     'duplex', 'duplex'), prob_calc('dimple', 'dimple'), prob_calc('cleft', 'cleft'))
