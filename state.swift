
struct State {
    
    let state: State?
    
    init(_ state: State) {
        self.state = state
    }
    
    func successor() -> State {
        State(self)
    }
    
    func predecessor() -> State? {
        self
    }
    
    func equals(_ other state: State) -> Bool {
        if other.state == nil {
	    return self.state == nil
	} else if self.state == nil {
	    return false
	} else {
            let p = self.predecessor()!
            let o = other.predecessor()!
            return p.equals(o)
        }
    }

    func plus(_ other: State) -> State {
	if other.state == nil {
	    return self.successor()
	} else {
	    let p = other.predecessor()
	    return self.plus(p).successor()
	}
    }

    func times(_ other: State) -> State {
        if other.state == nil {
	    return self
	} else {
	    let p = other.predecessor()
	    let c = self
	    return self.times(p).plus(c)
	}
    }
    
}




