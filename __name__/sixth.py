import fifth

print(fifth.main())


# here it doesnt run the fifth module.
# since in that module v perform condition.
# ie if __name__ == "__main__":
# bt here v run the python file(module) indirectly, so __name__ is set to that filename
# and in condition it is set to __main__. condition evaluats to False.
# thus this condition doesnt satisfy.
# so it returns nothing.

# so to run that v can either provide else condition and invoke the main() from that.
# or call that main() using the module name.
# ie., fifth.main()
