/**
 * 
 */

/**
 * @author gvenkat
 *
 */
public class AreaCalculator {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// Create a circle and print its area
		Circle aCircle = new Circle();

		System.out.println("Class Name: " + aCircle.returnClassName());
		System.out.println("Parent Class Name: " + aCircle.returnParentClassName());
		System.out.println("Class Name: " + aCircle.getDescription());

		double defaultArea =  aCircle.getArea();
		System.out.println("default area = " + defaultArea);

		aCircle.setRadius(2);
		//local variable
		double area = aCircle.getArea();
		System.out.println("Circle area = " + area);

		Shape circleShape = new Circle();
		System.out.println("Description of circle Shape: " + circleShape.getDescription());		

		System.out.println(" ***************************** ");
		// Create a triangle and print its area
		Triangle aTriangle = new Triangle();

		System.out.println("Class Name: " + aTriangle.returnClassName());
		System.out.println("Parent Class Name: " + aTriangle.returnParentClassName());
		System.out.println("Class Name: " + aTriangle.getDescription());

		double defaultTriArea =  aTriangle.getArea();
		System.out.println("default area = " + defaultTriArea);

		aTriangle.setBase(2);
		aTriangle.setHeight(4);
		//local variable
		double areaTri = aTriangle.getArea();
		System.out.println("triangle area = " + areaTri);

		Shape triangleShape = new Triangle();
		System.out.println("Description of triangle Shape: " + triangleShape.getDescription());
		System.out.println(" ***************************** ");

	}

}
