docs= {
    1 :"Document about python programming language and data analysis.",
    2: "Document discussing machine learning algorithms and programming techniques.",
    3: "Overview of natural language processing and its applications."
}
def build_index(docs):
    index={}
    for num,text in docs.items():
        terms=set(text.split())
        for x in terms:
            if x not in index:
                index[x]={num}
            else:
                index[x].add(num)
    return index
inverted_index=build_index(docs)
def boolean_and(operands,index):
    if not operands:
        return list(range(l,len(docs)+1))
    res=index.get(operands[0],set())
    for x in operands[1:]:
        res=res.intersection(index.get(x,set()))
    return list(res)
def boolean_or(operands,index):
    res=set()
    for x in operands:
        res=res.union(index.get(x,set()))
    return list(res)
def boolean_not(operand,index,total_docs):
    operand_set=set(index.get(operand,set()))
    all_docs_set=set(range(1,total_docs+1))
    return list(all_docs_set.difference(operand_set))
q1=["python"]
q2=["programming"]
r1=boolean_and(q1,inverted_index)
r2=boolean_or(q2,inverted_index)
r3=boolean_not("python programing",inverted_index,len(docs))
print("Documents containing 'python' and 'programing': ",r1)
