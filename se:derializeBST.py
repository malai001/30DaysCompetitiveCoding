class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res=dict()
        q=deque([(root,0)])
        while(len(q)):
            temp,pos=q.popleft()
            if temp:
                res[pos]=temp.val
                if(temp.left != None):
                    q.append((temp.left,2*pos+1))
                if(temp.right != None):
                    q.append((temp.right,2*pos+2))
            else:
                break
        return json.dumps(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        input_data=json.loads(data)
        nodes=dict()
        for pos,val in input_data.items():
            nodes[int(pos)] = TreeNode(val)
        
        for pos,node in nodes.items():
            l=2*pos+1
            r=2*pos+2
            if l in nodes:
                node.left=nodes[l]
            if r in nodes:
                node.right=nodes[r]
        return nodes[0] if len(nodes)>0 else None
