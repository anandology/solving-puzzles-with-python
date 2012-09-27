
def move(disks, src, dest, intermediate):
    if not disks:
        return
    move(disks[1:], src, intermediate, dest)
    movedisk(disks[0], src, dest)
    move(disks[1:], intermediate, dest, src)

def movedisk(disk, src, dest):
    print "move %d from %s to %s" % (disk, src, dest)

if __name__ == "__main__":
    move([3, 2, 1], "A", "B", "C")

