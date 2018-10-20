/**
 * This is an abstract class and cannot be instantiated directly
 * This must be inherited by a Child class
 */

/**
 * @author gvenkat
 *
 */
public abstract class Shape {
	
	//area is undefined for an abstract shape and hence
	//this method is marked abstract.  All Child classes
	//must provide the concrete implementation or the
	//Child class itself must be declared abstract
	public abstract double getArea();
	
	public String getDescription() {
		return "This is a generic Shape";
	}
		
	public String returnParentClassName() {
		String parent = this.getClass().getSuperclass().getSimpleName();
		return parent;
	}
	
	public String returnClassName() {
		String className = this.getClass().getSimpleName();
		return className;
	}
	
}
