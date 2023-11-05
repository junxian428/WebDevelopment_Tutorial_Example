namespace WebApplication1.Controllers
{
    using System.Collections.Generic;
    using Microsoft.AspNetCore.Cors;
    using Microsoft.AspNetCore.Mvc;

    [Route("api/[controller]")]
    [ApiController]
    [EnableCors]
    public class ItemsController : ControllerBase
    {
        // GET: api/items
        [HttpGet]
        public IActionResult Get()
        {
            var response = new { message = "Hello, API!" };
            return Ok(response);
        }

    }

}
